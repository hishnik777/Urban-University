My_dict = {'Vitaliy' : 35, 'Julia' : 42, 'Ilya' : 19}
print ('My_dict:', My_dict)

print('Existing value:', My_dict['Vitaliy'])

# My_dict['Polina'] = 18
# print (My_dict)
print('Not existing value:', My_dict.get('Polina'))

My_dict.update({'Roma' : 10, 'Vera' : 15})

a = My_dict.pop('Julia')
print ('Deleted value:', a)

print (My_dict)
