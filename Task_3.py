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
max_namber_list = give_int("Введите число (максимально возможный элемент массива): ")
rand_list = []
new_list = []
max_part = 0
min_part = 1
for i in range(0,namber):
    rand_list.append(round(random.uniform(0,max_namber_list),4))
    fractional_num = round((rand_list[i] % 1),4)  
    new_list.append(fractional_num)
    if max_part < new_list[i]:
        max_part = new_list[i]
    if min_part > new_list[i]:
        min_part = new_list[i]
    result = round((max_part - min_part),4)   
           
print(f'Разницу между максимальным {max_part} и минимальным {min_part} значением \nдробной части элементов массива \n{rand_list} равна: {result}') 