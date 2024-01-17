import json
import os


class Configurator:
    def __init__(self):
        #
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
    
    def list_connected_devices(self):
        pass
        

    def check_device_connectivity(self, device_ip):
        pass
