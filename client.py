from socket  import *
from constCS import * #-

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT)) # connect to server (block until accepted)
#s.send(str.encode('Hello, world'))  # send some data

print ("Insira os dados para operação desejada (sum, sub ou mul) seguindo o padrão:\n<operacao> <n1> <n2>.\nQuando quiser encerrar, digite 'fim'\n")

while True:
    msg= input ("")

    if msg.lower() == "fim": break

    s.send(msg.encode())
    data = s.recv(1024)     # receive the response
    
    print ("Resultado:", data.decode())            # print the result
s.close()               # close the connection
