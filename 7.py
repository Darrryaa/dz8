a = str(input('Введите целое число:'))
while a.isdigit() != True:
    a = input('Ошибка. Попробуйте еще раз. Введите число: ')
print('Введено целое число:',a)