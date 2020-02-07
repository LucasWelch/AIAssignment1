class Point:
    coordinates = ()

    def __init__(self, x, y):
        self.coordinates = (x, y)

    def get_coordinates(self):
        return self.coordinates

    def __str__(self):
        return "(" + str(self.coordinates[0]) + "," + str(self.coordinates[1]) + ")"
