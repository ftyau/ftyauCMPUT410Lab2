import socket
import sys
import thread

def clientthread(conn):
    while 1:
        data = conn.recv(1024)
        if not data:
            break
        stripped_data = str(data)[:len(data)-2]
        conn.sendall(stripped_data + " Frank\n")
    conn.close()

try:
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
except:
    print("Failed to create socket.")
    sys.exit()

print("Socket created.")

try:
    serversocket.bind(('', 8888))
except:
    print("Failed to bind.")
    sys.exit()

serversocket.listen(5)
print("Socket is now listening.")

while 1:
    (clientsocket, address) = serversocket.accept()
    thread.start_new_thread(clientthread, (clientsocket,))

serversocket.close()
