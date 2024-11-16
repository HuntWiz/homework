from itertools import combinations


def all_variants(text):
    for i in range(1, len(text)+1):
        out = ''
        
        yield out.join(str(x) for x in combinations(text, i))


a = all_variants("abc")
for i in a:
    print(i)