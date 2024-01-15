import paramiko
import os 
import time
import threading 
import queue 
import fnmatch

class SshClient:
    def __init__(self, hostname, username, password):
        self.hostname = hostname
        self.username = username
        self.password = password

    def connect(self):
        try:
            self.ssh_client = paramiko.SSHClient()
            self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh_client.connect(hostname=self.hostname, username=self.username, password=self.password)
        except paramiko.AuthenticationException as auth_exc:
            print(f"Authentication failed: {auth_exc}")
        except paramiko.SSHException as ssh_exc:
            print(f"SSH connection failed: {ssh_exc}")
        except Exception as exc:
            print(f"Error: {exc}")
        
    def disconnect(self):
        self.ssh_client.close()

    def send_file_via_sftp(self, local_file_path, remote_file_path):
        try:
            sftp_client = self.ssh_client.open_sftp()
            try:
                sftp_client.stat(remote_file_path)
                sftp_client.remove(remote_file_path)
            except FileNotFoundError:
                pass
            sftp_client.put(local_file_path, remote_file_path)
            sftp_client.close()
        except paramiko.SSHException as ssh_exc:
            print(f"SSH connection failed: {ssh_exc}")
        except Exception as exc:
            print(f"Error: {exc}")

    def download_file_via_sftp(self, remote_directory, file_pattern, local_directory):
        try:
            sftp_client = self.ssh_client.open_sftp()
            remote_files = sftp_client.listdir(remote_directory)
            for remote_file in fnmatch.filter(remote_files, file_pattern):
                remote_file_path = f'{remote_directory}/{remote_file}'
                local_file_path = f'{local_directory}/{remote_file}'
                sftp_client.get(remote_file_path, local_file_path)
            sftp_client.close()
        except paramiko.SSHException as ssh_exc:
            print(f"SSH connection failed: {ssh_exc}")
        except Exception as exc:
            print(f"Error: {exc}")

    def execute_ssh_command(self,  command):
        try:
            stdin, stdout, stderr = self.ssh_client.exec_command(command)
            #output = stdout.decode('utf-8')
            return stdout
        except paramiko.SSHException as ssh_exc:
            print(f"SSH connection failed: {ssh_exc}")
        except Exception as exc:
            print(f"Error: {exc}")

    def check_remote_file_existence(self, filepath):
        command = f'test -e {filepath} && echo "True" || echo "False"'
        stdout = self.execute_ssh_command(command)
        output = stdout.read().decode('utf-8').strip()
        return output
    
    def wait_until_csv_exist(self, remote_directory, file_pattern):
        try:
            csv_pattern_list = []
            sftp_client = self.ssh_client.open_sftp()
            while csv_pattern_list == []:
                remote_files = sftp_client.listdir(remote_directory)
                csv_pattern_list = fnmatch.filter(remote_files, file_pattern)
            sftp_client.close()
        except paramiko.SSHException as ssh_exc:
            print(f"SSH connection failed: {ssh_exc}")
        except Exception as exc:
            print(f"Error: {exc}")
 