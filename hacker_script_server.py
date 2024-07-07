
import socket

host = '127.0.0.1'
port = 9995

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket_server.bind((host, port))
socket_server.listen(1)


def wait_connect():

    print("listening......")

    client, client_conn_text = socket_server.accept()

    print(f"listen success : {client_conn_text}")

    recv_data = client.recv(1024).decode('utf-8')
    with open('./ip_address.txt' , 'w') as ip_address_file:
        ip_address_file.write(recv_data)
        print("ip was successful and write an file")

    socket_server.close()


if __name__ == '__main__':

    wait_connect()
