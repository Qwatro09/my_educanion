import threading
import time


class Knight(threading.Thread):

    def __init__(self, name, power):
        # threading.Thread.__init__(self)
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        my_day = 0
        enemy = 100
        while enemy > 0:
            enemy -= self.power
            time.sleep(1)
            my_day += 1
            print(f'{self.name} сражается {my_day} день(дня)..., осталось {enemy} воинов.\n')
        print(f'{self.name} одержал победу спустя {my_day} дней(дня)')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print(f'Все битвы закончились!')
