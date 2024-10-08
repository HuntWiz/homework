class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self):
        print("Модель "+self.__model)

    def get_horsepower(self):
        print("Мощность двигателя: "+str(self.__engine_power))

    def get_color(self):
        print("Цвет: "+self.__color)

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print("Нельзя сменить цвет на "+new_color)


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print("Владелец: {0}".format(self.owner))


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
vehicle1.print_info()

vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

vehicle1.print_info()
