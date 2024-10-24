class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def __init__(self):
        pass

    def get_products(self):

        try:
            file = open(self.__file_name, 'r')
        except IOError as e:
            file = open(self.__file_name, 'w')
            file.close()
            file = open(self.__file_name, 'r')

        s = file.read()
        file.close()
        return s

    def add(self, *products):
        s = self.get_products()
        file = open(self.__file_name, 'a')
        for i in products:
            if str(i) in s:
                print(f'Продукт {str(i)} уже есть в магазине')
            else:
                if file.tell() == 0:
                    file.write(str(i))
                else:
                    file.write('\n' + str(i))
        file.close()


s1 = Shop()

p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
