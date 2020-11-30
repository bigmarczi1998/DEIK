class Triangle:
    def __init__(self, p1, p2, p3=0):
        if p3 == 0:
            self.a = p1
            self.m = p2
        else:
            self.a = p1
            self.b = p2
            self.c = p3

    # K
    def perimeter(self):
        # ellenorizni tudjuk hogy az osztaly rendelkezik e az attributummal
        # c nevu attributum letezik e
        # T/F formatumba kapjuk meg
        if hasattr(self, "c"):
            return self.a + self.b + self.c
        else:
            return "A megadott parameterekkel nem szamolhato a kerulet!"

    # T
    def area(self):
        if hasattr(self, "c"):
            s = (self.a + self.b + self.c) / 2
            T = (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
            return T
        else:
            return (self.a * self.m) / 2

    # t1+t2 + muvelet feluldefinialasa
    # +
    def __add__(self, other):
        # lekerdezi, hogy melyik osztalynak/tipusnak a peldaja
        if isinstance(other, Triangle):
            return self.area() + other.area()
        elif isinstance(other, int) or isinstance(other, float):
            return self.area() + other

    # ha esetleg forditva adnad meg az operandusokat
    def __radd__(self, other):
        return self.__add__(other)

    # osszehasonlito feluldefinialassal
    # ==
    def __eq__(self, other):
        # True or False
        if isinstance(other, Triangle):
            return self.perimeter() == other.perimeter()
        else:
            return "A ket objektum nem osszehasonlithato!"

    # -
    def __sub__(self, other):
        if isinstance(other, Triangle):
            return self.area() - other.area()
        elif isinstance(other, int) or isinstance(other, float):
            return self.area() - other

    # not equal
    def __ne__(self, other):
        if isinstance(other, Triangle):
            return self.area() != other.area()
        else:
            return "A ket objektum nem osszehasonlithato!"

    # >
    def __gt__(self, other):
        if isinstance(other, Triangle):
            return self.area() > other.area()
        else:
            return "A ket objektum nem osszehasonlithato!"

    # <
    def __lt__(self, other):
        if isinstance(other, Triangle):
            return self.area() < other.area()
        else:
            return "A ket objektum nem osszehasonlithato!"


t1 = Triangle(3, 4, 5)
t2 = Triangle(4, 6, 3)
print(t1.area())
print(t2.perimeter())
print(t1 + 5)
print(5 + t1)
print(t1 == t2)
print(t1 - 4)
print(t1 != t2)
print(t1 > t2)
print(t1 < 1)
print(t1 == 'alma')
