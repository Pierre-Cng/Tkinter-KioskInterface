import zmq
import time
import sys 
context = zmq.Context()
socket = context.socket(zmq.PUB)

try:
    socket.bind("")
except Exception as e:
    print(f"Error binding to socket: {e}")
    sys.exit(1)

while True:
    try:
        topic = b"topic_A"
        message = b"Hello, subscribers!"
        socket.send_multipart([topic, message])
        time.sleep(1)
    except Exception as e:
        print(f"Error sending message: {e}")
