#Задача "Все ли равны?":
#На вход программе подаются 3 целых числа и записываются в переменные first, second и third соответственно. Ваша задача написать условную конструкцию (из if, elif, else), которая выводит кол-во одинаковых чисел среди 3-х введённых.

# Решение:

# Вводим последовательно три целых числа
first = int(input('Введите первое целое число: '))
second = int(input('Введите второе целое число: '))
third = int(input('Введите третье целое число: '))
# Задаем условия:
# если все три введенных целых числа одинаковые, то программа выводит число "3"
if first == second == third :
	print(3)
# если из трех введенных целых чисел два одинаковые, то программа выводит число "2"	
elif first == second or first == third or second == third :
	print(2)
# если все три введенных целых числа разные, то программа выводит число "0"
else:
	print(0)