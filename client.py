import socket
import plotly.express as px
import threading
import time


SWARM_ID = str(input("Enter Swarm id : "))
AGENT_ID= int(input("Enter Agent ID : "))
BUFF_SIZE = 1024
HOST = socket.gethostname()
PORT = 3454
z = []

class Client:
    def __init__(self):
        self.my_messages = []
        self.messages = []
        self.numbers = ['none']
        self.pheromone = [0]
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = HOST
        self.port = PORT
        self.sock.connect((self.host, self.port))
        print("Connected to Server ... ")
        self.connection_handler()



    def  connection_handler(self):
        while True:
            print("0 - to view cases and their Order")
            print("1X - request to add a suggestion to case X")
            print("2X - to view the current step in suggestion state in case X")
            print("3XY - to update the pheromone strength of suggestion Y in Case X")
            print("4X - to finalise the step in discussion in case X")
            print("5X - to view the solution of the case X")
            msg = input("You ---- ")
            self.sock.send(msg.encode('utf-8'))
            data = self.sock.recv(BUFF_SIZE).decode('utf-8')
            print(data)
            print(self.numbers)
            if data[0]=='2':
                x = data
                i = 0
                j = 0
                z = 1
                while i < len(x) and z > 0:
                    z = x.find('Suggestion ', i)
                    i = z + 1
                    if z > 0:
                        if self.numbers[0] == 'none':
                            self.numbers = []
                        self.numbers.append(x[z + 11])
                    y = x.find('Strength : ', j)
                    # 11 len of Strength
                    # print(y)
                    if y != -1:
                        b = x.find(' ', y + 11)
                        # print(float(x[y+11:b]))
                        if self.pheromone == [0]:
                            self.pheromone = []
                        self.pheromone.append(float(x[y + 11:b]))
                    j = y + 1
            fig = px.bar(x=self.numbers, y=self.pheromone)
            fig.write_html(str(AGENT_ID)+'.html', auto_open = True)

    def display(self):
        print("message set : ")
        print(self.messages)


client = Client()
