import _thread  #Modulo a ser importado para processamento assíncrono
import time  #Modulo time, utilizado para o delay do loop

max_loops = 5  #Quantidade maxima de loops para cada thread
num_thread = 0  #Quantidade de threads em execucao
thread_started = False  #Controle para saber sse ha alguma thread sendo executada

def task(task_name, delay=5):
    global max_loops, num_thread, thread_started

    num_thread += 1  #Adiciona 1 a quantidade de threads executadas
    thread_started = True  #Indica que há pelo menos uma thread sendo executada
    ct = 0  #Contador para o while

    while ct < max_loops:
        time.sleep(delay)  #Delayy para visualização do loop
        print("Thread: %s" %(task_name))  #Imprime o nome dado a thread
        ct += 1
    num_thread -=1  #Ao ser finalizado o loop, decrementa-se 1 a quantidade de threads em execucao

_thread.start_new_thread(task, (("Tarefa 1", 2)))  #Inicia uma nova thread utilizando a funcao task
_thread.start_new_thread(task, (("Tarefa 2", 10)))  #Inicia uma nova thread utilizando a funcao task

#Enquanto nenhuma thread estiver iniciada fica em loop infinito
while not thread_started:
    pass

#Enquanto pelo menos uma thread estiver iniciada fica em loop infinito, encerrando o programa em caso negativo
while num_thread > 0:
    pass