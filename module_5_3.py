class House:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def __len__(self):
        return self.floors

    def __str__(self):
        return "Название: "+self.name+", кол-во этажей: "+str(self.floors)

    def __eq__(self, other):
        if isinstance(other, House):
            return self.floors == other.floors
        else: print("Невозможно сравнить")

    def __lt__(self, other):
        if isinstance(other, House):
            return self.floors < other.floors
        else: print("Невозможно сравнить")

    def __le__(self, other):
        if isinstance(other, House):
            return self.floors <= other.floors
        else: print("Невозможно сравнить")

    def __gt__(self, other):
        if isinstance(other, House):
            return self.floors > other.floors
        else:
            print("Невозможно сравнить")

    def __ge__(self, other):
        if isinstance(other, House):
            return self.floors >= other.floors
        else:
            print("Невозможно сравнить")

    def __ne__(self, other):
        if isinstance(other, House):
            return self.floors != other.floors
        else:
            print("Невозможно сравнить")

    def __add__(self, value):
        if isinstance(value, int):
            self.floors += value
            return self
        else: print("Невозможно посчитать")

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

    def __sub__(self, value):
        if isinstance(value, int):
            self.floors = self.floors - value
            return self
        else:
            print("Невозможно посчитать")

    def __mul__(self, value):
        if isinstance(value, int):
            self.floors = self.floors * value
            return self
        else:
            print("Невозможно посчитать")

    def __rmul__(self, value):
        return self.__mul__(value)

    def __truediv__(self, value):
        if isinstance(value, int):
            self.floors = self.floors / value
            return self
        else:
            print("Невозможно посчитать")

    def __floordiv__(self, value):
        if isinstance(value, int):
            self.floors = self.floors // value
            return self
        else:
            print("Невозможно посчитать")


    def go_to(self, floor_num):
        if floor_num < 1 or floor_num > self.floors:
            print("Такого этажа не существует")
        else:
            for i in range(1, floor_num+1):
                print(i)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__