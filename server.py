#
# import socket
# from _thread import *
#
# # create a socket object
# serversocket = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
#
# # get local machine name
# host = socket.gethostname()
#
# port = 9991
#
#
# # bind to the port
# serversocket.bind((host, port))
#
# # queue up to 5 requests
# serversocket.listen(5)
# print("Server Waiting for connection")
# id = 0
# messages = []
# clients = ()
# clients = tuple(clients)
# def client_thread(conn):
#     global id, pos
#     conn.send(str(id).encode())
#     id = 1
#     reply= ' '
#     while True:
#         data= conn.recv(1024)
#         reply = data.decode('ascii')
#         messages.append(reply)
#         reply2 = str(messages)
#         if not data:
#             conn.send(str.encode('No data '))
#             break
#         else:
#             print("Recieved: "+reply)
#         conn.sendall(str.encode(reply2))
#     print("Connection closed for the Thread")
#     conn.close()
#
#
#
# while True:
#     conn, addr = serversocket.accept()
#     print("Connected to : ", addr)
#     start_new_thread(client_thread, (conn, ))





import socket
import threading
from _thread import *
import sys
import time
from case import *


SWARM_ID = str(input("Enter Swarm id : "))
AGENT_COUNT = int(input("Enter the no of agents in the swarm : "))
BUFF_SIZE = 1024

CHOICE_MESSAGE = ""

PORT = 34544

lock = threading.Lock()

class Server:
    def __init__(self):
        self.agents = []
        self.cases = []
        self.initialize_cases()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = socket.gethostname()
        self.port = PORT
        self.sock.bind((self.host, self.port))
        #self.sock.listen(5)
        threading.Thread(self.listener()).start()

    def initialize_cases(self):
        for i in range(0, 10):
            self.cases.append(Case())
            self.cases[i].case_id = str(i)
            self.cases[i].solution = []
            self.cases[i].final_step.suggestions= []


    def connection_handler(self, conn):
        while True:
            data = conn.recv(BUFF_SIZE).decode('utf-8')

            if data[0] == '0': #view the cases
                print("Request to view cases")
                conn.send(str(self.cases).encode('utf-8'))

            elif data[0] == '1': #add suggestion
                print("request to add a suggestional step")
                # conn.send("Enter suggestion starting with CASE number ".encode('utf-8'))
                # step_sugg = conn.recv(BUFF_SIZE).decode('utf-8')
                case_numbr = int(data[1])
                temp_step = Step()
                temp_step.step_id = 'step...id'
                temp_step.case_id = str(case_numbr)
                temp_step.data = data[2:]

                self.cases[case_numbr].final_step.add_suggestion(temp_step)
                print("Suggestion appended succesfully ")
                conn.send("Suggestion appended succesfully ".encode('utf-8'))
            elif data[0] == '2': #view steps
                print("request to view step suggestions")
                case_numbr = int(data[1])
                conn.send(str(self.cases[case_numbr].final_step.suggestions).encode('utf-8'))




            # print("Recieved ",data, " from ", conn)
            # self.steps.append(data)
            # conn.send(str(self.steps).encode('utf-8'))
            time.sleep(0.1)

    def listener(self):
        print("Server is running ... Waiting for connection ")
        for x in range(AGENT_COUNT):
            self.sock.listen(1)
            conn, addr = self.sock.accept()
            print("Agent ", addr," has Connected")
            self.agents.append(addr)
            #threading.Thread(target=self.agentthread, args=(conn, )).start()
            threading.Thread(target=self.connection_handler, args=(conn, )).start()

server = Server()
















