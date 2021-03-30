class Coordinate:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, coordinate_other):
        x_diff = (self.x - coordinate_other.x) ** 2
        y_diff = (self.y - coordinate_other.y) ** 2

        return (x_diff + y_diff) ** 0.5


if __name__ == '__main__':
    coordinate_1 = Coordinate(3, 30)
    coordinate_2 = Coordinate(4, 8)

    distance_coornidate_1 = coordinate_1.distance(coordinate_2)
    print(str(distance_coornidate_1))
