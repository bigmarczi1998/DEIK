class CIRCLE:

    def __init__(self, radius):
        self.r = radius

    def get_perimeter(self):
        import math
        return 2 * self.r * math.pi

    def get_area(self):
        import math
        return self.r ** 2 * math.pi

    def __str__(self):
        return "Radius: {}\nKerulet: {}\nTerulet: {}".format(self.r, self.get_perimeter(), self.get_area())


c1 = CIRCLE(3)
print(c1)
print(c1.get_area())
