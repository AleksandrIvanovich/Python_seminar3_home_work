#1- Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#Пример:
#[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random
def give_int(input_string):
    while True:
        try:
            num = int(input(input_string))
            return num
        except:
            print('Попробуйте еще раз. Вы ввели не число')
            
n = give_int("Введите число (количество элементов в списке):\n") 
user_list = []
summ = 0
for i in range(n):
    user_list.append(random.randint(-9,9))   
    if i == 1:
        summ = summ + user_list[i]
    else:
        if i % 2 != 0:
            summ = summ + user_list[i]  
            
print(user_list)  
print(f'Сумма элементов списка, стоящих на нечётной позиции равна {summ}')  