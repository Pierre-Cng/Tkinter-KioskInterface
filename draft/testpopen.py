import subprocess 
 
proc = subprocess.Popen(
        ["python", r"C:\Repository\tkinter-Kiosk-interface\data_flow.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True,  # Set this to True if 'python' is not in your PATH variable
        universal_newlines=True  # For text mode
    )

print(proc.stdout.readline())