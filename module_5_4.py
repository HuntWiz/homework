class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __del__(self):
        print("{0} снесён, но он останется в истории".format(self.name))
        

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
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)