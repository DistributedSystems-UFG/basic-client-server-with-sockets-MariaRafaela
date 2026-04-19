from socket  import *
from constCS import * #-
import random
import time
NUM_REQUISICOES = 100
OPERACOES = ["sum", "sub", "mul"]

tempo_total = 0
def gerar_requisicao():
    #Gera uma requisição aleatória no formato '<op> <n1> <n2>'.
    op = random.choice(OPERACOES)
    n1 = round(random.uniform(-100, 100), 2)
    n2 = round(random.uniform(-100, 100), 2)
    return f"{op} {n1} {n2}"

def modo_manual():
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
    s.close()     

def modo_automatico():
    global tempo_total
    tempo_total = 0
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((HOST, PORT))
    conn_start = time.perf_counter()
    for i in range(NUM_REQUISICOES):
        msg = gerar_requisicao()
        start = time.perf_counter()
        s.send(msg.encode())
        data = s.recv(1024) 
        end = time.perf_counter()
        tempo_resposta = end-start
        tempo_total += tempo_resposta
        #print ("Resultado:", data.decode(), f"Duracao: {(tempo_resposta*1000):.3f}")            # print the result
    conn_end = time.perf_counter()
    tempo_simulacao = conn_end-conn_start
    print(f"Tempo total: {(tempo_simulacao*1000)} Tempo médio: {tempo_total*1000/NUM_REQUISICOES}")



if __name__ == "__main__":

    print("Escolha o modo:")
    print("  1- Automático (gerador aleatório + paralelo)")
    print("  2- Manual (fornecer entrada)")
    escolha = input("> ").strip()

    if escolha == "1":
        modo_automatico()
    else:
        modo_manual()

              # close the connection
