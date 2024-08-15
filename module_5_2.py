class House:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def __len__(self):
        return self.floors

    def __str__(self):
        return "Название: "+self.name+", кол-во этажей: "+str(self.floors)

    def go_to(self, floor_num):
        if floor_num < 1 or floor_num > self.floors:
            print("Такого этажа не существует")
        else:
            for i in range(1, floor_num+1):
                print(i)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))