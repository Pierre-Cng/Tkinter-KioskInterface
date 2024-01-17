import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("")

# Subscribe to a specific topic
socket.setsockopt(zmq.SUBSCRIBE, b"topic_A")

while True:
    topic, message = socket.recv_multipart()
    print(f"Received message on topic {topic}: {message.decode('utf-8')}")
