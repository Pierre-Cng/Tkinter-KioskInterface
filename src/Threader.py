from Configurator import Configurator
import threading
import queue
import time 
from SshClient import SshClient
import os

class Threader:  
    def __init__(self, output_file):
        self.configurator = Configurator()
        self.output_queue = queue.Queue()
        self.output_file = output_file
        self.username = self.configurator.data['SSH_parameters']['username']
        self.password = self.configurator.data['SSH_parameters']['password']
        self.stop_event = threading.Event()
        self.threads = []

    def tail_file_over_ssh(self, hostname, dbc, stop_event):
        ssh_client = SshClient(hostname, self.username, self.password)
        ssh_client.connect()
        dbc_exist = ssh_client.check_remote_file_existence(f'~/CAN-CandumpDecoder/src/dbc/{dbc}.dbc')
        if dbc_exist == 'False':
            ssh_client.send_file_via_sftp(f'~/dbc/{dbc}.dbc', f'~/CAN-CandumpDecoder/src/dbc/{dbc}.dbc')
        ssh_client.execute_ssh_command(f'./start_recording.sh {dbc}')
        tail_exist = 'False' 
        while tail_exist == 'False':
            tail_exist = ssh_client.check_remote_file_existence('~/tail_*')
        stdout = ssh_client.execute_ssh_command("tail -F ./tail_*")
        while not stop_event.is_set():
            if stdout.channel.recv_ready():
                latest_output = stdout.channel.recv(1024).decode()
                self.output_queue.put(latest_output)
            else: 
                time.sleep(0.1)

    def kill_recording_process(self, hostname):
        ssh_client = SshClient(hostname, self.username, self.password)
        ssh_client.connect()
        ssh_client.execute_ssh_command('./stop_recording.sh')
        ssh_client.wait_until_csv_exist('.', '*.csv')
        ssh_client.download_file_via_sftp('.', f'{hostname}_*', os.getcwd())
        ssh_client.execute_ssh_command('./clean_logs.sh')

    def monitor_queue(self):
        with open(self.output_file, 'a') as file:
            while True:
                if not self.output_queue.empty():
                    data_line = self.output_queue.get()
                    file.write(data_line + '\n')

    def start_multithreading_data_capture(self, devices_conf):
        for device in devices_conf:
            thread = threading.Thread(target=self.tail_file_over_ssh, args=(device, devices_conf[device], self.stop_event))
            self.threads.append(thread)
            thread.start()
        monitor_thread = threading.Thread(target=self.monitor_queue)
        monitor_thread.start()
        self.threads.append(monitor_thread)

    def stop_multithreading_data_capture(self, devices_conf):
        self.stop_event.set()
        for thread in self.threads:
            thread.join()
        self.threads = []
        for device in devices_conf:
            thread = threading.Thread(target=self.kill_recording_process, args=(device))
            self.threads.append(thread)
            thread.start()
        for thread in self.threads:
            thread.join()

