# import requests
# from datetime import datetime
# from threading import Thread
#
# start_time = datetime.now()
# THE_URL = 'http://binaryjazz.us/wp-json/genrenator/v1/genre'
# res = []
#
# def func(url):
#     response = requests.get(THE_URL)
#     page_response = response.json()
#     res.append(page_response)
#
# thr_first = Thread(target=func, args=(THE_URL, ))
# thr_second = Thread(target=func, args=(THE_URL, ))
# thr_third = Thread(target=func, args=(THE_URL, ))
#
#
# thr_first.start()
# thr_second.start()
# thr_third.start()
#
# thr_first.join()
# thr_second.join()
# thr_third.join()
#
# print(res)
#

from time import sleep
from datetime import datetime
from threading import Thread


def write_words(word_count, file_name):
    with open(file_name, 'w',  encoding='utf-8') as file:
        for i in range(1, word_count+1):
            file.write(f"Какое-то слово № {i} \n" )
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")


start_time = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end_time = datetime.now()
fin_time = end_time - start_time
print(f'Работа потоков {fin_time}')


start_time = datetime.now()
thr_1 = Thread(target=write_words, args=(10, 'example5.txt'))
thr_2 = Thread(target=write_words, args=(30, 'example6.txt'))
thr_3 = Thread(target=write_words, args=(200, 'example7.txt'))
thr_4 = Thread(target=write_words, args=(100, 'example8.txt'))

thr_1.start()
thr_2.start()
thr_3.start()
thr_4.start()

thr_1.join()
thr_2.join()
thr_3.join()
thr_4.join()
end_time = datetime.now()
fin_time = end_time - start_time
print(f'Работа потоков {fin_time}')




