
def custom_write(file_name, strings):
    strings_positions = {}
    n = 0
    file = open(file_name, 'w', encoding='utf-8')

    for i in strings:
        n = n + 1
        strings_positions.update({(str(n), str(file.tell())):str(i)})
        file.write(i+'\n')
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)


