import time
import tkinter as tk
from threading import Thread


class Thread1(Thread):
    def __init__(self, priority=0, resources_to_reserve=tuple(), *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.daemon = True

        # Prioridade da task
        self.__priority = priority

        # Recursos que a task precisa reservar para rodar
        self.__resources_to_reserve = resources_to_reserve

    def run(self):
        print("Thread 1 START ------")
        print("Thread 1")
        time.sleep(0.5)
        print("Thread 1")
        time.sleep(0.5)
        print("Thread 1")
        time.sleep(0.5)
        print("Thread 1")
        time.sleep(0.5)
        print("Thread 1")
        time.sleep(0.5)
        print("Thread 1 END   ------")

    @property
    def priority(self):
        return self.__priority

    @ property
    def resources_to_reserve(self):
        return self.__resources_to_reserve


class Thread2(Thread):
    def __init__(self, priority=0, resources_to_reserve=tuple(), *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.daemon = True

        # Prioridade da task
        self.__priority = priority

        # Recursos que a task precisa reservar para rodar
        self.__resources_to_reserve = resources_to_reserve

    def run(self):
        print("Thread 2 START ------")
        print("Thread 2")
        time.sleep(0.5)
        print("Thread 2")
        time.sleep(0.5)
        print("Thread 2")
        time.sleep(0.5)
        print("Thread 2")
        time.sleep(0.5)
        print("Thread 2")
        time.sleep(0.5)
        print("Thread 2 END   ------")

    @property
    def priority(self):
        return self.__priority

    @property
    def resources_to_reserve(self):
        return self.__resources_to_reserve


class Thread3(Thread):
    def __init__(self, priority=0, resources_to_reserve: tuple = tuple(), *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.daemon = True

        # Prioridade da task
        self.__priority = priority

        # Recursos que a task precisa reservar para rodar
        self.__resources_to_reserve = resources_to_reserve

    def run(self):
        print("Thread 3 START ------")
        print("Thread 3")
        time.sleep(0.5)
        print("Thread 3")
        time.sleep(0.5)
        print("Thread 3")
        time.sleep(0.5)
        print("Thread 3")
        time.sleep(0.5)
        print("Thread 3")
        time.sleep(0.5)
        print("Thread 3 END   ------")

    @property
    def priority(self):
        return self.__priority

    @property
    def resources_to_reserve(self):
        return self.__resources_to_reserve


class MainWindow(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.after(10, self.__thread_1_handler)
        self.after(10, self.__thread_2_handler)

        self.__thread_1 = Thread1()
        self.__thread_2 = Thread2()
        self.__thread_3 = Thread3()

        # Cria um objeto scheduler para agendar as threads
        self.__scheduler = ThreadScheduler()

        # Lança a task do scheduler para controlar a execução das threads
        self.after(10, self.__scheduler_task)

    def __thread_1_handler(self):
        if not self.__thread_1.is_alive():
            self.__thread_1 = Thread1()
            self.__scheduler.add_thread_to_scheduler(self.__thread_1)
        self.after(10, self.__thread_1_handler)

    def __thread_2_handler(self):
        if not self.__thread_2.is_alive():
            self.__thread_2 = Thread2()
            self.__scheduler.add_thread_to_scheduler(self.__thread_2)
        self.after(10, self.__thread_2_handler)

    def __thread_3_handler(self):
        if not self.__thread_3.is_alive():
            self.__thread_3 = Thread3()
            self.__scheduler.add_thread_to_scheduler(self.__thread_3)
        self.after(10, self.__thread_3_handler)

    def __scheduler_task(self):
        """ Lança o scheluder para tratar o agendamento das threads """
        self.__scheduler.launch_scheduler()
        self.after(10, self.__scheduler_task)


class ThreadScheduler:

    def __init__(self):
        self.__threads_to_run = []
        self.__threads_running = []

    def launch_scheduler(self):
        """ Roda as threads levando em consideração os recursos reservados
        de uso exclusivo e a prioridade de cada thread """

        if self.__threads_to_run:
            # Se existem threads para rodar ...

            # Remove as threads que já terminaram de rodar da lista threads_running
            self.__threads_running = [thread for thread in self.__threads_running if thread.is_alive()]

            # Obtém a lista de recursos sendo utilizados pelas threads rodando
            resources_being_used = []
            for thread in self.__threads_running:
                resources_being_used.extend(thread.resources_to_reserve)

            # Roda as threads agendadas, priorizando as de maior prioridade entre aqualas que demandam
            # os mesmos recursos.
            for thread in tuple(self.__threads_to_run):
                # Para cada thread na lista de threads a rodar (iterando da maior para menor prioridade)
                if all(resource not in resources_being_used for resource in thread.resources_to_reserve):
                    # Se todos os recursos demandados pela thread agendada para rodar estão disponíveis
                    thread.start()
                    self.__threads_to_run.remove(thread)
                    self.__threads_running.append(thread)
                    resources_being_used.extend(thread.resources_to_reserve)

    def add_thread_to_scheduler(self, new_thread):
        """ Adiciona uma nova thread a lista do scheduler """
        if type(new_thread) not in [type(thread) for thread in self.__threads_to_run]:
            # Se a nova thread a ser agendada ainda não existe na lista de threads para rodar...
            # Adiciona a nova thread a lista
            self.__threads_to_run.append(new_thread)

            # Reordena a lista de threads a rodar de acordo com a prioridade de cada thread (maior primeiro)
            self.__threads_to_run.sort(key=lambda thread: thread.priority, reverse=True)

    @property
    def threads_to_run(self):
        """ Retorna uma lista com as threads aguardando para rodar """
        return self.__threads_to_run


if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()

