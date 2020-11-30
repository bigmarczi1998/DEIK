class SZAMLISTA:
    def __init__(self, lista):
        self.lista = lista

    def sum_zero(self):
        result_list = []
        for i in range(len(self.lista)):
            for j in range(i + 1, len(self.lista)):
                for k in range(j + 1, len(self.lista)):
                    if self.lista[i] + self.lista[j] + self.lista[k] == 0:
                        result_list.append([self.lista[i], self.lista[j], self.lista[k]])
        print(result_list)


szamok = SZAMLISTA([-25, -10, -7, -3, 2, 4, 8, 10])
szamok.sum_zero()

# ctrl alt L
