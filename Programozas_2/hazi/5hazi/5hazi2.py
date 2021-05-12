class Busz:
    def __init__(self, rendszam, max_utasok=50, napi_koltseg=10000):
        self.__rendszam = rendszam
        self.__max_utasok = max_utasok
        self.__napi_koltseg = napi_koltseg

    def set(self, rendszam, max_utasok, napi_koltseg):
        self.__rendszam = rendszam
        self.__max_utasok = max_utasok
        self.__napi_koltseg = napi_koltseg

    def get(self):
        return (self.__rendszam, self.__max_utasok, self.__napi_koltseg)

    def __str__(self):
        return ("Rendszam: {}\nMax utasszám: {}\nNapi költség: {}".format(self.__rendszam, self.__max_utasok,
                                                                          self.__napi_koltseg))


class Buszsofor:
    def __init__(self, nev, kor, jegyar=50):
        self.__nev = nev
        self.__kor = kor
        self.__jegyar = jegyar

    def set(self, nev, kor, jegyar):
        self.__nev = nev
        self.__kor = kor
        self.__jegyar = jegyar

    def get(self):
        return (self.__nev, self.__kor, self.__jegyar)

    def __str__(self):
        return ("Név: {}\nKor: {}\nJegyár: {}".format(self.__nev, self.__kor, self.__jegyar))


class Buszjarat(Busz, Buszsofor):
    def __init__(self, rendszam, nev, kor, max_utasok=50, napi_koltseg=10000, jegyar=500):
        Busz.__init__(rendszam, max_utasok, napi_koltseg)
        Buszsofor.__init__(nev, kor, jegyar)
        self.jelenlegi_utasok_szama = 0
        self.napi_bevetel = 0
        self.max_utasok = max_utasok
        self.napi_koltseg = napi_koltseg
        self.jegyar = jegyar

    def megallo(self, felszallo_utasok, leszallo_utasok, ):
        if self.jelenlegi_utasok_szama > 0 and self.jelenlegi_utasok_szama - leszallo_utasok >= 0:
            self.jelenlegi_utasok_szama -= leszallo_utasok
        else:
            return ("A busz kiürült!")
        if self.jelenlegi_utasok_szama < self.max_utasok and self.jelenlegi_utasok_szama + felszallo_utasok <= self.max_utasok:
            self.napi_bevetel = felszallo_utasok * self.jegyar
            self.jelenlegi_utasok_szama += felszallo_utasok
        else:
            return ("A busz megtelt!")

    def profit(self):
        self.napi_bevetel -= self.napi_koltseg
        if self.napi_bevetel <= 0:
            return "Mai napon még nem ért el profitot!"
        else:
            return self.napi_bevetel


b = Busz("MPJ-779")
print(b)
b.set("LMX-802", 50, 5000)
print(b.get())
print(b.__str__())

bs = Buszsofor("Mézes B. Ödön", 45)
