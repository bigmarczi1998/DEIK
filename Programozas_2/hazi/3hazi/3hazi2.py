class Henger:
    def __init__(self, r, m):
        self.r = r
        self.m = m
        self.A = 0
        self.V = 0

    def felszin(self):
        import math
        self.A = round(2 * self.r * math.pi + 2 * self.r * math.pi * self.m, 2)
        return self.A

    def terfogat(self):
        import math
        self.V = round(math.pi * self.r ** 2 * self.m, 2)
        return self.V

    def __str__(self):
        return self.r, self.m, self.felszin(), self.terfogat()

    def __add__(self, other):
        if isinstance(other, Henger):
            return round(self.V + other.V, 2)
        elif isinstance(other, int) or isinstance(other, float):
            return round(self.V + other.V, 2)

    def __sub__(self, other):
        if isinstance(other, Henger):
            return round(self.V - other.V, 2)
        elif isinstance(other, int) or isinstance(other, float):
            return round(self.V - other.V, 2)

    def __mul__(self, other):
        if isinstance(other, Henger):
            return round(self.V * other.V, 2)
        elif isinstance(other, int) or isinstance(other, float):
            return round(self.V * other.V, 2)

    def __eq__(self, other):
        return self.m == other.m

    def __ne__(self, other):
        return self.m != other.m

    def __gt__(self, other):
        return self.m >= other.m

    def __lt__(self, other):
        return self.m <= other.m


h1 = Henger(5, 25)
h2 = Henger(10, 12)
print("Az első henger adatai:", h1.__str__())
print("A második henger adatai:", h2.__str__())
print(h1 + h2)
print(h2 - h1)
print(h1 * h2)
print(h1 == h2)
print(h1 != h2)
print(h1 > h2)
print(h1 < h2)
