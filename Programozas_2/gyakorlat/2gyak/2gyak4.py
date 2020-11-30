# ket metodosu osztaly

class SZOVEG:
    str = "Ez az alapertelmezett string"

    def __init__(self):
        pass

    def set_string(self):
        self.str = input("Kerek egy uj stringet: ")

    def print_string(self):
        print(self.str.upper())


s1 = SZOVEG()
print(s1.str)
s1.set_string()
s1.print_string()
