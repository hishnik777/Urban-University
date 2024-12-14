
# Работа со словарями:

my_dict = {'Vitaliy' : 35, 'Julia' : 42, 'Ilya' : 19}
print ('Dict:', my_dict)

print('Existing value:', my_dict['Vitaliy'])

# my_dict['Polina'] = 18
# print (my_dict)
print('Not existing value:', my_dict.get('Polina'))

my_dict.update({'Roma' : 10, 'Vera' : 15})

a = my_dict.pop('Julia')
print ('Deleted value:', a)

print ('Modified dictionary:', my_dict)


# Работа с множествами:

my_set = {1, 2, 3, 4, 5, 1, 2, 3, True, False, 'Апельсин', 'Банан', 'Клубника', 3.14, (4, 6, 7), 'Банан', 3.14, True}
print('Set:', my_set)

my_set.update(["754", "Ананас"])

my_set.discard('Банан')

print('Modified set:', my_set)
