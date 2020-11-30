# Osztalyok hiearchiaja
# Ős-osztály
# UML diagram


# Ez az Ős-osztály
class Polygon:
    side_length = []

    def __init__(self, n):
        self.sides = n

    def input_sides(self):
        for i in range(self.sides):
            side = int(input('Kerem az {}. oldal hosszat: '.format(i + 1)))
            self.side_length.append(side)

    def disp_sides(self):
        for i in range(self.sides):
            print('Az {}. oldal hossza: {}'.format(i + 1, self.side_length[i]))


# Ez lesz a Polygon osztály leszármazottatja
class Triangle(Polygon):
    # ()be irva a hivatkozás
    # Ős-osztályra való hivatkozás
    # Őszosztaly_neve.input_sides(self)
    # super().input_sides()
    def __init__(self):
        # Polygont meghivva 3 legyen a oldal szama
        Polygon.__init__(self, 3)

    def triangle_check(self):
        a, b, c = self.side_length[0], self.side_length[1], self.side_length[2]
        if (a + b <= c) or (a + c <= c) or (b + c <= a):
            return False
        return True

    # felulirjuk az alap Polygon osztalyban irt metodust
    def input_sides(self):
        # akkor ugrik ki a ciklusbol, ha szerkeztheto a 3szog
        while True:
            # az elozofeladat miatt kell kiuritenunk a listat
            self.side_length = []
            # ososztalyra hivatkozas maskeppen, es csak bekerjuk az oldalakat
            super().input_sides()
            if self.triangle_check():
                break
            else:
                print('Hibas oldalhosszak')
                break

    # mar nem a feladat resze
    def get_perimeter(self):
        res = 0
        for i in range(self.sides):
            res += self.side_length[i]
        print('Kerulete a haromszognek:', res)


p1 = Polygon(5)
p1.input_sides()
p1.disp_sides()

t2 = Triangle()
t2.input_sides()
t2.disp_sides()
t2.get_perimeter()
