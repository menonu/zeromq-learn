#!/usr/bin/env python3

import zmq
import time

import random


def event_loop(socket):
    while True:
        message = socket.recv()
        print('recv', message)
        time.sleep(1)




def main():
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect("tcp://localhost:21000")
    socket.setsockopt(zmq.SUBSCRIBE, b'')

    event_loop(socket)


if __name__ == '__main__':
    print('hi')
    main()
