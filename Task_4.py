#N = int(input("Введите размер списка: "))
import random
def give_int(input_string):
    while True:
        try:
            num = int(input(input_string))
            return num
        except:
            print('Попробуйте еще раз. Вы ввели не число')
k = give_int("Введите размер списка: ")           
spam = list(range(1, k+1))
print(spam)