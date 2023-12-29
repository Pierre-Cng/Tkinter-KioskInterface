import subprocess 

proc = subprocess.Popen(['python', 'data_flow.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

print(proc.stdout.read())