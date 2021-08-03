import socket
import numpy as np


def process():
    return np.zeros(1)


if __name__ == '__main__':

    ADDRESS = 'localhost'
    PORT = 10000

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = (ADDRESS, PORT)
    print('Starting up server on {}:{}'.format(*address))
    sock.bind(address)
    sock.listen(1)

    while True:
        print('Waiting for connection')
        connection, client_address = sock.accept()
        print('Connection accepted!')

        try:
            while True:
                # Wait for client to send a message, even if it's purely for synchronization
                master_buffer = connection.recv(1024)

                # # If client message required, convert to array
                # array = np.fromstring(master_buffer, dtype=np.float64)

                # Create an array and send it to the client
                array = process()
                connection.sendall(array.tostring())
        finally:
            connection.close()
            print('Connection terminated, waiting for new connection...')