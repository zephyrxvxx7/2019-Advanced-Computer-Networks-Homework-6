import zmq
import random

#  Prepare our context and sockets
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:8787")

topicfilter = random.randrange(1, 10)
socket.setsockopt_string(zmq.SUBSCRIBE, f"{topicfilter}")

print(f"Subscribe topic {topicfilter}")

#  Do 10 requests, waiting each time for a response
while True:
    string = socket.recv_string()
    _, messagedata = string.split(' ', 1)
    print(f"Received a message: {messagedata}")
