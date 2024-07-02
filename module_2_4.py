numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
count = 0
next = -1

for i in numbers:
    next += 1
    if numbers[next] == 1:
        continue
    for j in range(1, numbers[next]+1):
        if numbers[next] % j == 0:
            count += 1
            #if count > 2 or (j != 1 and j != numbers[next]):
                #break
    if count == 2:
        primes.append(numbers[next])
    else:
        not_primes.append(numbers[next])
    count = 0

print('Primes:', primes)
print('not Primes:', not_primes)
