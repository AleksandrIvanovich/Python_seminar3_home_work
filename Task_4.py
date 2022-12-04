#4- Напишите программу, которая будет преобразовывать десятичное число в двоичное. 
# Подумайте, как это можно решить с помощью рекурсии.Не использовать функцию bin
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10
def give_int(input_string):
    while True:
        try:
            num = int(input(input_string))
            return num
        except:
            print('Попробуйте еще раз. Вы ввели не число')
number = give_int('Введите целое число: ')
z =  give_int('Введите целое число (число системы в которую нужно перевести число): ') 
result_list = []
num = number
while num != 0:
    if num - (num // z)*z >= 1:
        result_list.insert(0,(num - (num // z)*z))
        num = num // z
    if num - (num // z)*z == 0:
        result_list.insert(0,0)    
        num = num // z      
else:
    result = " ".join(map(str,result_list[1:]))
    
print(f'Число {number} в системе измерения {z} равно: {result}.')