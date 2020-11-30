class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __str__(self):
        return "<{},{}>".format(self.x, self.y)

    def __add__(self, other):
        # ha az other az vektor tipusu akkor
        if isinstance(other, Vector):
            self.x += other.x
            self.y += other.y
            # a def selfre hivatkozunk ilyenkor
            return self
        elif isinstance(other, int) or isinstance(other, float):
            self.x += other  # int miatt nem kell .x
            self.y += other
            return self

    # rmul, rsub az a reverse

    # ez a metodus meghivja/tovabbitja
    def __iadd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        if isinstance(other, Vector):
            self.x *= other.x
            self.y *= other.y
            return self
        elif isinstance(other, int) or isinstance(other, float):
            self.x *= other
            self.y *= other
            return self

    def __eq__(self, other):
        return self.__abs__() == other.__abs__()

    def __ne__(self, other):
        return self.__abs__() != other.__abs__()

    def __gt__(self, other):
        return self.__abs__() > other.__abs__()

    def __lt__(self, other):
        return self.__abs__() < other.__abs__()


v1 = Vector(2, 3)
v2 = Vector(1, 1)
print(abs(v1))
print(v1 + v2)
# ha + helyett +=
# v3 = (v1 += 2)
print(v1 * v2)
print(v1 == v2)
