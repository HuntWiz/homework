def calculate_structure_sum(*args):
    global summ
    for i in args[0]:
        if isinstance(i, list) or isinstance(i, tuple):
            summ = calculate_structure_sum(i)
        if isinstance(i, dict):
            summ = calculate_structure_sum(i)
            summ = summ + sum(i.values())
        if isinstance(i, set):
            summ = calculate_structure_sum(i)

        if isinstance(i, int):
            summ = summ + i
        elif isinstance(i, str):
            summ = summ + len(i)

    return summ


summ = 0
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)