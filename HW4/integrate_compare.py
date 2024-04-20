import logging
import math
import time
import concurrent.futures
from itertools import repeat

logging.basicConfig(level=logging.INFO, filename='integration_logs.log')

#v1
# def integrate(f, a, b, n_iter=10000000):
#     acc = 0
#     step = (b - a) / n_iter
#     for i in range(n_iter):
#         acc += f(a + i * step) * step
#     return acc

# def integrate_parallel(f, a, b, n_jobs=1, n_iter=10_000_000):
#     n_iter = int(n_iter / n_jobs)
#     step = (b - a) / n_jobs
#     a_values = [a + step*i for i in range(n_jobs)]
#     b_values = [a + step*i for i in range(1, n_jobs+1)]

#     start_time = time.time()
#     with concurrent.futures.ThreadPoolExecutor(max_workers=n_jobs) as executor:
#         sum(executor.map(integrate, repeat(f),  a_values, b_values, repeat(n_iter)))

#     total_time = time.time() - start_time
#     logging.info(f"Thread workers: {n_jobs}, Execution time: {total_time} sec")


#     with concurrent.futures.ProcessPoolExecutor() as executor:
#         sum(executor.map(integrate, repeat(f),  a_values, b_values, repeat(n_iter)))

        
#     total_time = time.time() - start_time
#     logging.info(f"Process workers: {n_jobs}, Execution time: {total_time} sec")

# v2
def integrate_parallel(f, a, b, *, n_jobs=1, n_iter=10000000):

    def calculate_partition(f, a, b, n_iter, n_jobs, partition):
        acc = 0
        step = (b - a) / n_iter
        length = n_iter // n_jobs
        start = partition * length
        end = min(start + length, n_iter)
        for i in range(start, end):
            acc += f(a + i * step) * step
        return acc
        
    start_time = time.time()
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {executor.submit(calculate_partition, f, a, b, n_iter, n_jobs, i): i for i in range(n_jobs)}
        concurrent.futures.wait(futures)
        
    total_time = time.time() - start_time
    logging.info(f"Thread workers: {n_jobs}, Execution time: {total_time} sec")
    
    start_time = time.time()
    
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = {executor.submit(calculate_partition, f, a, b, n_iter, n_jobs, i): i for i in range(n_jobs)}
        concurrent.futures.wait(futures)
        
    total_time = time.time() - start_time
    logging.info(f"Process workers: {n_jobs}, Execution time: {total_time} sec")

cpu_num = 8
if __name__ == '__main__':
    # main()
    for n_jobs in range(1, cpu_num * 2 + 1):
        logging.info(f"n_jobs = {n_jobs}")

        integrate_parallel(math.cos, 0, math.pi / 2, n_jobs=n_jobs)
        logging.info("_"*50)

