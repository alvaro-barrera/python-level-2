class Car:

    def __init__(self, model, brand, color):
        self.model = model
        self.brand = brand
        self.color = color
        self._status = 'stopped'
        self._engine = Engine(cylindres=4)

    def sped_up(self, type='slowly'):
        if type == 'fast':
            self._engine.fuel_inyection(10)
        else:
            self._engine.fuel_inyection(3)


class Engine:
    def __init__(self, cylindres, type='gasoline'):
        self.cylindres = cylindres
        self.type = type
        self._temperature = 0

    def fuel_inyection(self, quantity):
        pass


def run():
    pass

if __name__ == '__main__':
    run()

