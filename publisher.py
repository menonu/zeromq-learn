#!/usr/bin/env python3

import zmq
import time

import random


def event_loop(socket):
    while True:
        num = random.randint(0, 10)
        socket.send_string("{0} {0}".format(num))
        time.sleep(1)
        print('sending')




def main():
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://*:21000")

    event_loop(socket)


if __name__ == '__main__':
    print('hi')
    main()
