
import threading

lock = threading.Lock() # Trava

def thread_function():
    lock.acquire()  # Bloqueia o recurso
    try:
        # Região Crítica
        print("Thread está executando")
    finally:
        lock.release()  # Libera o lock

thread1 = threading.Thread(target=thread_function)
thread2 = threading.Thread(target=thread_function)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
