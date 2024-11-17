def is_prime(func):
    def wrapped(one, two, three):
        sum = func(one, two, three)
        k = 0
        for i in range(1, sum+1):
            if sum%i == 0:
                k+=1
        if k == 2:
            return 'Простое'+'\n'+str(sum)
        else:
            return 'Составное'+'\n'+str(sum)
    return wrapped


@is_prime
def sum_three(one, two, three):
    sum = one + two + three
    return sum




print(sum_three(2,3,6))