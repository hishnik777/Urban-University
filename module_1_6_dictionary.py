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
