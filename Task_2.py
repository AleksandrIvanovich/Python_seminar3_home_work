#2-Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#[2, 3, 4, 5, 6] => [12, 15, 16];
#[2, 3, 5, 6] => [12, 15]

import random
def give_int(input_string):
    while True:
        try:
            num = int(input(input_string))
            return num
        except:
            print('Попробуйте еще раз. Вы ввели не число')
            
n = give_int("Введите число (количество элементов в списке):\n") 
l = n//2
user_list = []
for i in range(n):
    user_list.append(random.randint(1,10)) 
    list_centr = user_list[l::l+1]
    left_part = user_list[:l]
    rigth_part = (user_list[:: -1])[:l]

result_list = []    
for i in range(l):
    if len(result_list) < l:
        result_list.append((left_part[i])*(rigth_part[i]))           
if n % 2 == 1:
    result_list.append((list_centr[0])**2)
          
print(user_list)
print(result_list)