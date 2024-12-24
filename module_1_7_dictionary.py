# Задание "Средний балл":

#	Список: grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]

#	Множество: students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

#	{'Aaron': 4.0, 'Bilbo': 2.25, 'Johhny': 4.0, 'Khendrik': 3.6666666666666665, 'Steve': 4.8}

# Решение:

# Зададим исходные данные
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print(students)
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
print(grades)
# Преобразуем множество студентов в список
students = list({'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'})
print(students)
# Отсортируем список студентов по алфавиту (получим список ключей нашего словаря)
key_list = sorted(students)
print(key_list)
# Найдем средний балл каждого ученика (средее арифметическое значение каждого списка оценок)
grades_middle = [sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]), sum(grades[2])/len(grades[2]), sum(grades[3])/len(grades[3]), sum(grades[4])/len(grades[4])]
print(grades_middle)
# Составим из двух списков (студенты и оценки) словарь, где ключами будут имена студентов из заданного списка, а значениями - соответствующий средний бал каждого ученика
dict_grades_middle = dict(zip(key_list, grades_middle))
print(dict_grades_middle)