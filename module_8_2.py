

def personal_sum(numbers):
    sum = 0
    incorrect_data = 0
    try:
        for i in numbers:
            try:
                sum += i
            except TypeError as exc:
                incorrect_data += 1
                print(f'Некорректный тип данных для подсчёта суммы -{i}')
    except TypeError as exc:
        print('В numbers записан некорректный тип данных')
        return None

    return sum, incorrect_data


def calculate_average(numbers):
    k = 0
    sum = 0
    try:
        sum = personal_sum(numbers)[0]
        for i in numbers:
            if isinstance(i, int) or isinstance(i, float):
                k += 1
    except:
        avarage = 0
    try:
        average = sum/k
    except ZeroDivisionError as exc:
        average = 0

    return average

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать