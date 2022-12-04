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
a = give_int('Введите целое число: ')  
b = give_int('Введите целое число: ') 
list = []
result = 0         
def converting_num(a, b):
    ost = a % b
     
    if ost !=0:
        result = a // b
        list.insert(0,ost)
    return result
    #     if number % sistema == 1:
    #         list.append(1)
    #     return    
    # number = converting_num
    # return list 
    
print(list)
print(result)