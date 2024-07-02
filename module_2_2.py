first = input()
second = input()
third = input()
print(first, second, third)

if first == second and second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)