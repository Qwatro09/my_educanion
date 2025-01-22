import time
from time import sleep
import threading


def wite_words(word_count, file_name):
    with open(file_name, "a", encoding='utf-8') as file:
        for num in range(1, word_count + 1):
            file.write(f'Какое-то слово № {num} \n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


start = time.time()

wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')

finish = time.time()
print(f'Время работы функций {(finish - start):.5f}')

start_1 = time.time()

thread_1 = threading.Thread(target=wite_words, args=(10, 'example5.txt'))
thread_2 = threading.Thread(target=wite_words, args=(30, 'example6.txt'))
thread_3 = threading.Thread(target=wite_words, args=(200, 'example7.txt'))
thread_4 = threading.Thread(target=wite_words, args=(100, 'example8.txt'))

thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()

thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()

finish_1 = time.time()
print(f'Время работы потоков {(finish_1 - start_1):.5f} секунд')
