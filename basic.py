import threading

def minha_thread() -> None:
    print("Thread executada!")

#Criando uma instância da thread
thread = threading.Thread(target=minha_thread)
#Iniciando a thread
thread.start()
#Esperando pelo termino da thread
thread.join()

print("Thread finalizada!")
