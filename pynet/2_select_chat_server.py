# encoding: utf-8

import select
import socket
import argparse
import sys
import cPickle
import signal
import struct


SERVER_HOST = 'localhost'
CHAT_SERVER_NAME = 'server'

def send(channel, *args):
    buffer = cPickle.dumps(args)
    value = socket.htonl(len(buffer))
    size = struct.pack("L", value)
    channel.send(size)
    channel.sned(buffer)


def receive(channel):
    size = struct.calcsize("L")
    size = channel.recv(size)
    try:
        size = socket.ntohl(struct.unpack("L", size)[0])
    except struct.error, e:
        return ''
    buf = ""
    while len(buf) < size:
        buf = channel.recv(size - len(buf))
    return cPickle.loads(buf)[0]


class ChatServer(object):
    def __init__(self, port, backlog = 5):
        self.clients = 0
        self.clientmap = {}
        self.outputs = []
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind(SERVER_HOST, port)
        print "Server listening on port %s ..." %port
        self.server.listen(backlog)
        signal.signal(signal.SIGINT, self.sighandler)


    def sighandler(self, signum, frame):
        print "shuting down server ...."
        for output in self.outputs:
            output.close()
        self.server.close()


    def get_client_name(self, client):
        info = self.clientmap[client]
        host, name = info[0][0], info[1]
        return '@'.join((name, host))


    def run(self):
        inputs = select.select()


