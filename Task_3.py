#3-Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов.
#Пример:
#[1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
#[4.07, 5.1, 8.2444, 6.98] - 0.91 или 91
import random 

def give_int(input_string):
    while True:
        try:
            num = int(input(input_string))
            return num
        except:
            print('Попробуйте еще раз. Вы ввели не число')

namber = give_int("Введите число (колличество элементов в массиве): ")
namber_list = give_int("Введите число N(диапазон массива от -N до N): ")
n = give_int("Введите число (количество цифр после точки): ")
rand_list = []
new_list = []
max_part = 0
min_part = 1
for i in range(0,namber):
    rand_list.append(round(random.uniform((namber_list)*-1,namber_list),n))
    fractional_num = round((abs(rand_list[i]) % 1),n)  
    new_list.append(fractional_num)
    if max_part < new_list[i]:
        max_part = new_list[i]
    if min_part > new_list[i]:
        min_part = new_list[i]
    result = round((max_part - min_part),n)   
           
print(f'Разницу между максимальным {max_part} и минимальным {min_part} значением \nдробной части элементов массива \n{rand_list} равна: {result}') 