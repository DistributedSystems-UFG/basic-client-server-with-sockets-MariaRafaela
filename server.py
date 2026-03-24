from socket  import *
from constCS import * #-

s = socket(AF_INET, SOCK_STREAM) 
s.bind(('0.0.0.0', PORT))  #-
s.listen(1)           #-
(conn, addr) = s.accept()  # returns new socket and addr. client 
while True:                # forever
  data = conn.recv(1024)   # receive data from client
  if not data: break       # stop if client stopped

  msg= bytes.decode(data).strip()

  strings= msg.split()
  operacao= strings[0]
  x= float(strings[1])
  y= float(strings[2])

  if operacao == "sum": resultado= x + y
  elif operacao == "sub": resultado= x - y
  elif operacao == "mul": resultado= x * y
  else: resultado= "Não identificado. Forneça uma operação (sum, sub ou mul) no formato: <operação> <n1> <n2>"

  conn.send(str(resultado).encode())
  #print(bytes.decode(data))
  #conn.send(str.encode(bytes.decode(data)+"*")) # return sent data plus an "*"
conn.close()               # close the connection
