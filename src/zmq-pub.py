import zmq
import time

context = zmq.Context()
publisher = context.socket(zmq.PUB)
publisher.bind("tcp://*:5555")

# Send a start message to all slaves
publisher.send_string("start")

# Allow time for slaves to process the start message
time.sleep(2)

# Receive data from all slaves
while True:
    data = publisher.recv_string()
    print(f"Received data from a device: {data}")
