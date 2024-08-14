#1
immutable_var = (1, 7, "object", [1, 5])
print (immutable_var)
print (immutable_var[1])

#2
#immutable_var [0] = 4
#print (immutable_var)
#Кортеж не поддерживает обращение по элементам (нельзя изменить элементы кортежа).
#При этом, можно изменить значение изменяемого объекта (типа) кортежа:
immutable_var [3][0]= 4 # изменим четвертый объект кортежа (индекс [3]), а именно первый элемент внутреннего списка (индекс[0]) с "1" на "4".
print (immutable_var)

#3
mutable_list = [1, 7, "object", [1, 5]]
mutable_list [2] = 8 # изменим третий элемент (индекс[2]) заданного списка с "object" на "8".
print(mutable_list )