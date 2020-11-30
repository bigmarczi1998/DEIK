# UML diagram
# Osztaly es modell felirasa, reprezentalasa

# Osztalyszintu attributumok
# Osztalyokat attributumokkal toltunk fel
# init metodus maga lesz a konstruktor
# parameter listaban self mindig pekdanyositaskent

class SZAM:
    def __init__(self, num):
        self.n = num

    # elso konstruktor
    def square_n(self):
        return self.n ** 2

    def pow_k(self, k):
        return self.n ** k

    def abs_value(self):
        if self.n >= 0:
            return self.n
        else:
            return -self.n  # vesszuk a n -1xet


szam1 = SZAM(5)
print(szam1.square_n())
print(szam1.pow_k(3))
print(szam1.abs_value())
