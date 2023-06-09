# Вариант 15.
# Натуральные числа, расположенные в порядке возрастания.
# Для каждой такой последовательности минимальное число вывести прописью.
import re

dict = {0: 'ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь',
        9: 'девять'}
min_num = 0
check = 1
b = []
file = open("input.txt", "r")
marks = '''!()-[]{};?@#№$%:'"\,./^&amp;*_'''


def num_to_words(n):  # вывод числа словами
    for j in range(len(min_num)):
        for l in dict:
            if str(l) == min_num[j]:
                print(dict[l], end=' ')
                break


while True:  # пока файл не пустой:
    a = file.readline().split()
    if not a:  # если файл кончился
        print('\nКонец файла')
        break
    for j in a:  # читаем число из файла
        for x in j:  # читаем число
            if x in marks:  # читаем знаки
                j = j.replace(x, "")  # если есть какой-то знак - меняем его на пустоту
        res = re.findall(r'0{1}|^[1-9]*[0-9]+',j)  # числа от 0 до 9 включительно и числа начинающиеся с цифры от 1 до 9
        if len(res) == 1 and len(j) == len(res[0]) and len(j) > 0:  # проверяем есть ли оно
            if check == 1 or b[-1] < int(res[0]):  # если число больше предыдущего - последовательность есть
                b.append(int(res[0]))  # добавляем число в массив
                check -= 1
            elif b[-1] > int(res[0]): # если число меньше предыдущего - конец последовательности
                print(b) # выводим массив
                min_num = str(min(b))
                num_to_words(min_num)
                print('')
                b = [int(res[0])]  # начало следующей последовательности

    print(b)  # выводим последний массив и минимальное число
    min_num = str(min(b))
    num_to_words(min_num)
