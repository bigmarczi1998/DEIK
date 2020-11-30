class Auto:
    def __init__(self, uzemanyagszint, fogyasztas_100km):
        self.uzemanyagszint = int(uzemanyagszint)
        self.fogyasztas_100km = int(fogyasztas_100km)

    def tankolas(self):
        hozzaadott_uzemanyag = int(input("Hány litert tankolunk a kocsiba: "))
        self.uzemanyagszint += hozzaadott_uzemanyag
        return self.uzemanyagszint

    def vezetes(self):
        vegso_tankolas = int(self.tankolas())
        megtett_km = int(input("Hány km fog megtenni az autó: "))
        if ((megtett_km / 100) * self.fogyasztas_100km) <= vegso_tankolas:
            tankszint = vegso_tankolas - ((megtett_km / 100) * self.fogyasztas_100km)
            return '{:.0f} liter az üzemanyagszint az utazás végén.'.format(tankszint)
        else:
            return 'Ki fog fogyni a benzin.'


f1 = Auto(20, 8)
print(f1.vezetes())
