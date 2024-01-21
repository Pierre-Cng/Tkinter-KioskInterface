import threading
import zmq 
import time 
import time
import threading 
import json
import os
from queue import Queue
import sys 

class Configurator:
    def __init__(self):
        self.get_config_backup()

    def get_config_backup(self):
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config_backup.json'), 'r') as file:
            self.data = json.load(file)

class TcpManager:
    def __init__(self):
        self.configure_sockets()

    def configure_sockets(self):
        self.context = zmq.Context()
        self.pub_socket = self.context.socket(zmq.PUB)
        self.router_socket = self.context.socket(zmq.ROUTER)
        try:
            self.pub_socket.bind('tcp://*:5558')
            self.router_socket.bind('tcp://*:5559')
        except Exception as e:
            sys.exit()

    def identify_request(self, device_dict, label):
        self.pub_request('identify', 'requested')
        displayed_line_list = []
        for attempt in range(5):
            try:
                address, id, message = self.router_socket.recv_multipart(zmq.DONTWAIT)
                line = f'{message.decode()} - connected - {device_dict[message.decode()]}'
                if line not in displayed_line_list:
                    displayed_line_list.append(line)
            except zmq.Again:
                pass
            if displayed_line_list == []:
                label.set('Waiting for response...')
            else:
                label.set("\n".join(displayed_line_list))
            time.sleep(1)

    def start_request(self, message_queue, stop_event):
        self.pub_request('start', 'requested')
        id_list = []
        while not stop_event.is_set():
            try:
                address, id, message = self.router_socket.recv_multipart(zmq.DONTWAIT)
                if id not in id_list:
                    message_queue.put(message.decode())
                    id_list.append(id)
            except zmq.Again:
                pass

    def pub_request(self, topic, message):
        for attempt in range(10):
            try:
                self.pub_socket.send_multipart([topic.encode(), message.encode()])
                time.sleep(0.5)
            except Exception as e:
                print(f'Error sending message: {e}')

    def receive_data(self):
        try:
            address, id, message = self.router_socket.recv_multipart(zmq.DONTWAIT)
            tuple = (address, id, message)
            return tuple
        except zmq.Again:
            pass

    def cleanup(self):
        self.pub_socket.close()
        self.router_socket.close()
        self.context.term()

    '''
    def start_request(self, data_queue):
        instruction = 'instruction'
        self.pub_request('start', instruction)
        self.stop_event.clear()
        self.stream_thread = threading.Thread(target=self.receive_data, args=(data_queue, self.stop_event))
        self.stream_thread.daemon = True
        self.stream_thread.start()
    '''
       
    def stop_request(self):
        self.pub_request('stop', 'requested')
        self.stop_event.set()
        
        #from the other side send file when seeing this 
        # message will be decoded can trace messages 
        # use candumpdecoder repo to use the function of putting message into dictionnary self.signals 
        # or output in queue qnother threqd for dictionnqry 
        # qnd plot

class RequestThreader:
    def __init__(self):
        pass

    def thread_function(self, target, args): 
        data_flow_thread = threading.Thread(target=target, args=args)
        data_flow_thread.daemon = True 
        data_flow_thread.start()
        return data_flow_thread
    
    def identify_request(self, device_dict, label):
        self.tcpmanager = TcpManager()
        self.tcpmanager.identify_request(device_dict, label)
        self.tcpmanager.cleanup()

    def start_request(self, message_queue, stop_event):
        self.tcpmanager = TcpManager()
        self.tcpmanager.start_request(message_queue, stop_event)
        self.tcpmanager.cleanup()

    def thread_identify_request(self, device_dict, label):
        thread = self.thread_function(self.identify_request, (device_dict, label))

    def thread_start_request(self, message_queue, stop_event):
        thread = self.thread_function(self.start_request, (message_queue, stop_event))
