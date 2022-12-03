
def give_int(input_string):
    while True:
        try:
            num = int(input(input_string))
            return num
        except:
            print('Попробуйте еще раз. Вы ввели не число')

namber = give_int("Введите число N: ")
numbers_list = []
for i in range(1, namber+1):
    if i == 1:
        numbers_list.append(i)
    else:
        new_element = numbers_list[i-2]*i
        numbers_list.append(new_element)
print (f"Набор произведений чисел от 1 до {namber}: {numbers_list}")