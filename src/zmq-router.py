import zmq

context = zmq.Context()
dealer_socket = context.socket(zmq.DEALER)
dealer_socket.setsockopt(zmq.IDENTITY, b"dealer")
dealer_socket.connect("tcp://192.168.0.0:5555") #dummy example

# Receive the general message from the ROUTER
message_from_router = dealer_socket.recv_string()
print(f"Received message from ROUTER ({message_from_router.decode()}")

# Simulate processing and send a response back to the ROUTER
#dealer_socket.send_multipart([dealer_identity, b"", b"Response from DEALER"])