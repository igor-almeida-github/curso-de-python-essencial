"""
Python Paralelismo
"""
import time
import multiprocessing

lista = list(range(10000000))


def quadrado(n):
    return n ** 2


if __name__ == "__main__":
    # Processamento sequêncial
    start = time.time()
    serie = list(map(quadrado, lista))
    stop = time.time()
    print(f'CPU SEQUÊNCIAL: {(stop - start):.10f}s')
    t1 = stop - start

    # Processamento paralelo
    pool = multiprocessing.Pool()
    start = time.time()
    paralelo = pool.map(quadrado, lista)
    stop = time.time()
    print(f'CPU PARALELO: {(stop - start):.10f}s')
    t2 = stop - start
    print(f'Percentual de redução de tempo de processamento: {100 * (t1 - t2) / t1:.2f}%')


