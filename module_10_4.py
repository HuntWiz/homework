import random
import threading
import time
from queue import Queue


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        time.sleep(random.randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        free_tables = False
        for guest in guests:  # проверка на наличие столов
            for table in self.tables:
                if table.guest is None:
                    free_tables = True
                    break
                if table.guest is not None:
                    free_tables = False

            if free_tables:
                for table in self.tables:  # если есть столы - проверяем какой свободный и садим
                    if table.guest is None:
                        table.guest = Guest(guest)
                        table.guest.name = guest.name
                        table.guest.start()
                        print(f"{guest.name} сел(-а) за стол номер {table.number}")
                        break

            if not free_tables:  # нет стола - в очередь
                print(f'{guest.name} в очереди')
                self.queue.put(guest)

    def discuss_guests(self):
        unless_one_table = True
        while not self.queue.empty() or unless_one_table == True:

            for table in self.tables:
                if table.guest is not None:
                    if not table.guest.is_alive():
                        print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                        print(f'Стол номер {table.number} свободен')
                        table.guest = None
                if not self.queue.empty() and table.guest is None:
                    guest = self.queue.get()
                    table.guest = Guest(guest)
                    table.guest.name = guest.name
                    print(f"{guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
                    table.guest.start()

            for table in self.tables:
                if table.guest is not None:
                    unless_one_table = True
                    break
                if table.guest is None:
                    unless_one_table = False


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
