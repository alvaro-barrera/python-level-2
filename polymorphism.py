class Person:

    def __init__(self, name):
        self.name = name

    def moving(self):
        print('Ando caminando')


class Cyclist(Person):

    def __init__(self, name):
        super().__init__(name)

    def moving(self):
        print('Ando moviendome en mi bicicleta')


def run():
    person = Person('David')
    person.moving()

    cyclist = Cyclist('Daniel')
    cyclist.moving()


if __name__ == '__main__':
    run()
