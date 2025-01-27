import random
import time
import threading


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for x in range(1, 101):
            plus = random.randint(50, 500)
            with self.lock:
                self.balance += plus
                print(f'Пополнение номер {x}: {plus}. Баланс: {self.balance}')
                if self.balance >= 500 and not self.lock.locked():
                    self.lock.release()
            time.sleep(0.001)

    def take(self):
        for y in range(1, 101):
            minus = random.randint(50, 500)
            print(f'Запрос на снятие номер {y} на сумму {minus}')
            self.lock.acquire()
            if minus <= self.balance:
                self.balance -= minus
                print(f'Снятие: {minus}. Баланс: {self.balance}')
            else:
                print(f'Запрос {y} отклонён, недостаточно средств')
            self.lock.release()
            time.sleep(0.001)


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'\nИтоговый баланс: {bk.balance}')
