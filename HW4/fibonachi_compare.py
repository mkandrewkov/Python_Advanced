
"""
Взять функцию подсчета чисел Фибоначчи и сравнить время исполнения кода 
(вызова функции от большого числа n (чтобы была видна разница в запусках на потоках и процессах) 10 раз, 
каждая на отдельном потоков\процессов) при использовании threading и multiprocessing. Запускаем одновременно 10 потоков/процессов, 
сравниваем общее время.
Необходимо сравнить время выполнения при синхронном запуске, использовании потоков и процессов. 

Использовать concurrent.futures нельзя, задача про другое!
Артефакт - текстовый файл с результатами запуска различными методами.
"""
import time
from typing import Union
import threading
import  multiprocessing


def fibonacci(n:int):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_parallel(n:int, 
                       obj:Union[threading.Thread, multiprocessing.Process], 
                       Event:Union[threading.Event, multiprocessing.Event], 
                       n_jobs:int = 8):
    start_time = time.time()
    paralells = []
    
    ev = Event()
    for _ in range(n_jobs):
        p = obj(target=fibonacci, args=(n,))
        paralells.append(p)
        p.start()

    ev.set()

    for p in paralells:
        p.join()
    
    end_time = time.time()
    return end_time - start_time

def fibonacci_sequently(n:int, n_jobs:int = 8):

    start_time = time.time()

    for _ in range(n_jobs):
        result = fibonacci(n)
    
    end_time = time.time()
    return end_time - start_time
    

# n = 24
replays = 1
n_jobs = 10



# Выполняем каждый метод 10 раз и записываем результаты в файл
with open('fibonacci_performance.txt', 'w') as file:
    for n in [5, 10, 14, 20, 21, 22, 23,  24, 30, 31, 32, 33, 34, 35]:
        file.write(f"Number n = {n} \n")

        file.write("Sequentially: For-loop:\n")
        for _ in range(replays):
            time_taken = fibonacci_sequently(n)
            file.write(f"Время выполнения: {time_taken}\n")
        
        file.write("\n Parallel: Threading:\n")
        for _ in range(replays):
            time_taken_t = fibonacci_parallel(n, threading.Thread, threading.Event, n_jobs=n_jobs)
            file.write(f"Время выполнения: {time_taken_t}\n")

        file.write("\n Parallel: Multiprocessing:\n")
        for _ in range(replays):
            time_taken_p = fibonacci_parallel(n, multiprocessing.Process, multiprocessing.Event, n_jobs=n_jobs)
            file.write(f"Время выполнения: {time_taken_p}\n")
        if time_taken_p > time_taken_t:
            file.write(f"\n Отношение времени: {round(time_taken_p / time_taken_t, 3) }\n")
        else:
            file.write(f"\n Отношение времени: {round(time_taken_t / time_taken_p, 3) }\n")

        file.write("__"*100+"\n")


        
