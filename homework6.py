my_dict = {'Login': 'mymommy', 'Password': 52}
print(my_dict)
print(my_dict.get('Login'), my_dict.get('Name'))
my_dict.update({'Name': 'Pablo',
                'Subname': 'Mundo'})
print('Удаленное значение:',my_dict.pop('Login'))
print(my_dict)

my_set = {1, 2, 3, 3, 'list', 'book', 'list'}
print(my_set)
my_set.add(5)
my_set.add('mount')
my_set.discard(3)
print(my_set)
