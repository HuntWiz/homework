immutable_var = 'homework', 5, True
List = [1,2,3, 'Home']
print(immutable_var)
#immutable_var[0] = 'Work' не будет работать, так как кортеж неизменяемый обьект
# Кортеж можно лишь сложить с другим кортежем или умножить
# При этом кортеж может иметь изменяемые обьекты внутри себя
mutable_list = ['list', 123, True]
mutable_list[0] = 12
print(mutable_list)