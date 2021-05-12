class Ember:
    def __init__(self, nev, kor, nrg):
        self.nev = nev
        self.kor = kor
        self.nrg = nrg

    def sleep(self, h):
        self.nrg += h * 10
        if self.nrg > 100:
            self.nrg = 100
            return self.nrg
        else:
            return self.nrg

    def work(self, h):
        self.nrg -= h * 10
        if self.nrg < 0:
            self.nrg = 0
            return self.nrg
        else:
            return self.nrg

    def __str__(self):
        print("Név: ", self.nev, "\nÉletkor: ", self.kor, "\nEnergiaszint: ", self.nrg)

    def __eq__(self, other):
        if isinstance(other, Ember):
            return self.nrg == other.nrg
        else:
            return "A két objektum nem összehassonlítható!"

    def __ne__(self, other):
        if isinstance(other, Ember):
            return self.nrg != other.nrg
        else:
            return "A két objektum nem összehassonlítható!"

    def __lt__(self, other):
        if isinstance(other, Ember):
            return self.nrg <= other.nrg
        else:
            return "A két objektum nem összehassonlítható!"

    def __gt__(self, other):
        if isinstance(other, Ember):
            return self.nrg > other.nrg
        else:
            return "A két objektum nem összehassonlítható!"


class Hallgato(Ember):
    def __init__(self, neptun_kod, tan_atlag):
        Ember.__init__(self, nev, kor, nrg)
        self.kod = neptun_kod
        self.avg = tan_atlag

    def zh_iras(self, zh_ido):
        import numpy as np
        self.work(zh_ido)
        jegy = np.random.randint(1, 5, size=1)
        return jegy, self.nrg

    def __eq__(self, other):
        if isinstance(other, Hallgato):
            if self.avg == other.avg:
                return self.nrg == other.nrg
            else:
                return self.avg == other.avg
        else:
            return "A két objektum nem összehassonlítható!"

    def __ne__(self, other):
        if isinstance(other, Hallgato):
            if self.avg == other.avg:
                return self.nrg != other.nrg
            else:
                return self.avg != other.avg
        else:
            return "A két objektum nem összehassonlítható!"

    def __lt__(self, other):
        if isinstance(other, Hallgato):
            if self.avg == other.avg:
                return self.nrg <= other.nrg
            else:
                return self.avg <= other.avg
        else:
            return "A két objektum nem összehassonlítható!"

    def __gt__(self, other):
        if isinstance(other, Hallgato):
            if self.avg == other.avg:
                return self.nrg > other.nrg
            else:
                return self.avg > other.avg
        else:
            return "A két objektum nem összehassonlítható!"

    def __str__(self):
        print("Neptun kód: ", self.kod, "\nTanulmányi átlag: ", self.avg)


nev = "Mézes B. Ödön"
kor = 20
nrg = 50
e = Ember(nev, kor, nrg)
e.sleep(8)
e.work(5)
e.__str__()
neptun_kod = "DGER4S"
tan_atlag = 4.6
h = Hallgato(neptun_kod, tan_atlag)
h.zh_iras(2)
h.__str__()
