import threading
import time


def timer():
    time.sleep(1)


class Knight(threading.Thread):
    ENEMY = 100

    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f"{self.name}, на нас напали!")
        days = 0
        while self.ENEMY > 0:
            self.ENEMY -= self.power
            timer()
            days += 1
            print(f"{self.name} сражается {days}..., осталось {self.ENEMY} воинов. \n")
        print(f"{self.name} одержал победу спустя {days} дней(дня)! \n")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print("Война...война никогда не меняется")
