import socket;

server_address = ('', 8080)

listen_to_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

"""AF_INIT is for IPV4
    SOCK_STREAM Stands for TDP"""

listen_to_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

"""SOL_SOCKET is the socket layer itself
Reuse flag set to true (1) helps the ip and port to be available on 
 TIME_WAIT state even after connection is closed. Anything incoming can make use
 of this wait period"""

listen_to_socket.bind(server_address)
listen_to_socket.listen(1)

print('Http is active on port ')

"""Waiting for a connection. Accept returns an open connection
between client and server. Accept returns a pair of address and connection """

print('Waiting for a connection...')

while True:
    c_connection, c_address = listen_to_socket.accept()
    request = c_connection.recv(1024)
    response = b"""\
    HTTP/1.1 200 OK

    Successfully Connected!
    """
    if request == "":
        break
    else:
        print('Sending data back to client')
        c_connection.sendall(response)
    c_connection.close()
