import time
from threading import Thread


contador = 50_000_000


def contagem_regressiva(n):
    while n > 0:
        n -= 1


inicio = time.time()
t1 = Thread(target=contagem_regressiva(contador), args=(contador//2,))
t2 = Thread(target=contagem_regressiva(contador), args=(contador//2,))
t1.start()
t2.start()
t1.join()
t2.join()
fim = time.time()

print(f'Tempo em segundos: {fim - inicio}')

# O uso de multithread é limitado pelo GIL, pois ele prejudica a utilização de multi-cores
# Em caso de necessitarmos de multi-processing, ver o arquivo multi_processing
