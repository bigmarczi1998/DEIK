class RECTANGLE:

    def __init__(self, ao, bo):
        self.a = ao
        self.b = bo

    def get_perimeter(self):
        return 2 * (self.a + self.b)

    def get_area(self):
        return self.a * self.b

    def __str__(self):
        return "a hossz: {}\nb hossz: {}\nKerulet: {}\nTerulet: {}".format(self.a, self.b, self.get_perimeter(),
                                                                           self.get_area())


p = RECTANGLE(3, 4)
print(p)
# print(p.get_area())
# print(p.get_perimeter())
