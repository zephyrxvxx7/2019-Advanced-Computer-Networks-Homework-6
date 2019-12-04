import zmq


def main():
    """ main method """

    context = zmq.Context()

    # Socket facing clients
    frontend = context.socket(zmq.XPUB)
    frontend.bind("tcp://*:8787")

    # Socket facing services
    backend = context.socket(zmq.XSUB)
    backend.bind("tcp://*:5487")

    zmq.proxy(frontend, backend)

    # We never get here…
    frontend.close()
    backend.close()
    context.term()


if __name__ == "__main__":
    main()
