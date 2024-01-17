import zmq
import time

context = zmq.Context()
master_pub = context.socket(zmq.PUB)
master_pub.bind("tcp://*:5555")

master_router = context.socket(zmq.ROUTER)
master_router.bind("tcp://*:5555")

# Send a start message to all slaves
master_pub.send_string("start")

# Allow time for slaves to process the start message
time.sleep(2)

# Receive data from all slaves
while True:
    identity, data = master_router.recv_multipart()
    print(f"Received data from a slave ({identity.decode()}): {data.decode()}")
