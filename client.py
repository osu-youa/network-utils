#!/usr/bin/env python

import rospy
import socket
import numpy as np


def do_stuff(msg):

    # Even if you don't need to communicate with the server, send a message anyway to indicate that you're waiting
    data = np.zeros(0)
    sock.sendall(data.tostring())
    response = np.fromstring(sock.recv(1024), dtype=np.float64)

    # Do something with the response
    dummy_pub.publish()


if __name__ == '__main__':

    ADDRESS = 'localhost'
    PORT = 10000

    name = 'generic_client'
    rospy.init_node(name)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = (ADDRESS, PORT)

    def shutdown():
        sock.close()
        print('Socket closed...')
    rospy.on_shutdown(shutdown)

    sock.connect(address)
    rospy.loginfo('Connected to socket at {}:{}!'.format(*address))

    rospy.Subscriber('/dummy_topic', DummyMsg, do_stuff)
    dummy_pub = rospy.Publisher('/dummy_pub', DummyMsg)
    rospy.spin()


