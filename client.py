import socket
import threading
import time

SWARM_ID = str(input("Enter Swarm id : "))
AGENT_ID= int(input("Enter Agent ID : "))
BUFF_SIZE = 1024
HOST = socket.gethostname()
PORT = 34544

class Client:
    def __init__(self):
        self.my_messages = []
        self.messages = []
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = HOST
        self.port = PORT
        self.sock.connect((self.host, self.port))
        print("Connected to Server ... ")
        self.connection_handler()
        # threading.Thread(target=self.recieving_msg()).start()
        # threading.Thread(target = self.sending_msg()).start()


    # def sending_msg(self):
    #     while True:
    #         msg = input("You ---- : ")
    #         self.sock.send(msg.encode('utf-8'))
    #         self.my_messages.append(msg)
    #
    # def recieving_msg(self):
    #     while True:
    #         print("I started ...")
    #         data = self.sock.recv(BUFF_SIZE).decode('utf-8')
    #         self.messages.append(data)
    #         self.display()

    def  connection_handler(self):
        while True:
            print("0 - to view cases and their Order")
            print("1X - request to add a suggestion to case X")
            print("2X - to view the current step in suggestion state in case X")
            print("3XY - to update the pheromone strength of suggestion Y in Case X")
            print("4X - to finalise the step in discussion in case X")
            
            msg = input("You ---- ")
            self.sock.send(msg.encode('utf-8'))
            data = self.sock.recv(BUFF_SIZE).decode('utf-8')
            print(data)

    def display(self):
        print("message set : ")
        print(self.messages)


client = Client()
