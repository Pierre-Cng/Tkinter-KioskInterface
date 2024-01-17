import threading
import zmq 
import time 
import time
import threading 
import json
import os

class Configurator:
    def __init__(self):
        self.get_config_backup()

    def get_config_backup(self):
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config_backup.json'), 'r') as file:
            self.data = json.load(file)
    
    def displayed_config_info(self):
        connected_devices = self.list_connected_devices()
        displayed_info =''
        for key, value in self.data['Devices'].items():
            if key in connected_devices:
                state = 'connected'
            else:
                state = 'disconnected'
            displayed_info += f"{key}: {value} - {state}\n" 
        return displayed_info

class TcpManager:
    def __init__(self):
        self.host_list = {}
        self.configure_sockets()
        self.stop_event = threading.Event()

    def configure_sockets(self):
        context = zmq.Context()
        self.pub_socket = context.socket(zmq.PUB)
        self.router_socket = context.socket(zmq.ROUTER)
        try:
            self.pub_socket.bind('tcp://*:5555')
            self.router_socket.bind('tcp://*:5556')
        except Exception as e:
            print(f'Error binding to socket: {e}')
    
    def pub_request(self, topic, message):
        for attempt in range(5):
            try:
                self.pub_socket.send_multipart([topic.encode(), message.encode()])
                time.sleep(0.5)
            except Exception as e:
                print(f'Error sending message: {e}')

    def scan_network(self):
        self.pub_request('identity', 'requested')
        for update in range(20):
            address, message = self.router_socket.recv_multipart()
            # message will be hostname
            self.host_list[message.decode()] = address
        return self.host_list

    def receive_data(self, data_queue, stop_event):
        while not stop_event.is_set():
            address, message = self.router_socket.recv_multipart()
            data_queue.put(message.decode())

    def start_request(self, data_queue):
        instruction = ''
        self.pub_request('start', instruction)
        self.stop_event.clear()
        self.stream_thread = threading.Thread(target=self.receive_data, args=(data_queue, self.stop_event))
        self.stream_thread.daemon = True
        self.stream_thread.start()
       
    def stop_request(self):
        self.pub_request('stop', 'requested')
        self.stop_event.set()
        
        #from the other side send file when seeing this 
        # message will be decoded can trace messages 
        # use candumpdecoder repo to use the function of putting message into dictionnary self.signals 
        # or output in queue qnother threqd for dictionnqry 
        # qnd plot
