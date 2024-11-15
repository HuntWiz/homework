first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(x)-len(y) if len(x)>len(y) else len(y)-len(x)
                for x, y in zip(first, second)
                if not len(x) == len(y))
second_result = (len(first[x]) == len(second[x]) for x in range(len(second)))

print(list(first_result))
print(list(second_result))



