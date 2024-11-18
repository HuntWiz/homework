import random
import threading
import time


class Bank(threading.Thread):
    def __init__(self, balance=0):
        threading.Thread.__init__(self)
        self.balance = balance
        self.lock = threading.Lock()

    def timer(self):
        time.sleep(0.001)

    def deposit(self):
        for i in range(1, 101):
            print(f'{i} транзакция пополнения')
            new_deposite = random.randint(50, 500)
            self.balance += new_deposite
            print(f"Пополнение: {new_deposite}. Баланс: {self.balance}")
            if self.lock.locked() and self.balance >= 500:
                self.lock.release()
            self.timer()

    def take(self):
        for i in range(1, 101):
            print(f'{i} транзакция списания')
            new_taking = random.randint(50, 500)
            print(f"Запрос на списание {new_taking}")
            if self.balance >= new_taking:
                self.balance -= new_taking
                print(f"Снятие: {new_taking}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()



bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')