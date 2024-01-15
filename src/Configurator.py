import nmap
import json
import os
class Configurator:
    def __init__(self):
        self.nm = nmap.PortScanner()
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
        connected_devices = []
        start_ip = self.data['Hotspot_parameters']['start_ip']
        end_ip = self.data['Hotspot_parameters']['stop_ip'] 
        ip_range = f"{start_ip}-{end_ip}"
        # Scan your network to find connected devices
        self.nm.scan(hosts=ip_range, arguments='-sn -T5')
        for host in self.nm.all_hosts():
            connected_devices.append((host, self.nm[host].hostname()))
        return connected_devices

    def check_device_connectivity(self, device_ip):
        try:
            self.nm.scan(hosts=device_ip, arguments='-Pn')  # Disable host discovery and directly scan the specified IP
            if device_ip in self.nm.all_hosts():
                host_status = self.nm[device_ip]['status']['state']
                return (device_ip, host_status)
            else:
                return (device_ip, 'disconnected')
        except Exception as e:
            print(f"Error: {e}")
