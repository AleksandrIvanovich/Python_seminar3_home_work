#5-Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.
#Пример:
#для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
def give_int(input_string):
    while True:
        try:
            num = int(input(input_string))
            return num
        except:
            print('Попробуйте еще раз. Вы ввели не число')

namber = give_int("Введите число N: ")
fibonachi_list = []
fibonachi_list.insert(0,0)
fibonachi_list.insert(1,1)
for i in range(2, namber+1):
    if i >= 2:
        new_element = fibonachi_list[i-2]+fibonachi_list[i-1]
        fibonachi_list.append(new_element)
          
new_list = []
for i in range(len(fibonachi_list)):
    if i != 0 and i % 2 !=1:
        new_element = fibonachi_list[i]*-1
        new_list.append(new_element)
    else:
        new_element = fibonachi_list[i]
        new_list.append(new_element)
        
new_list_reverse = (new_list[1:])[:: -1]       
result_list = new_list_reverse + fibonachi_list
 
print(result_list)
      
