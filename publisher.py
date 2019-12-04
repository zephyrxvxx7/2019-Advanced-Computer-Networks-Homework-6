import zmq
import random
import time

#  Prepare our context and sockets
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.connect("tcp://localhost:5487")

publisher_id = random.randrange(0,9999)
while True:
    topic = random.randrange(1,10)
    messagedata = f"Hello, there is server#{publisher_id}"
    print(f"Send: {topic} {messagedata}")

    socket.send_string(f"{topic} {messagedata}")
    time.sleep(0.1)
