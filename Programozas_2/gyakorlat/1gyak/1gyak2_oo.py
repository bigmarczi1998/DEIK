class Piramis:
    def __init__(self, num):
        self.n = num

    def epit(self):
        for i in range(1, self.n + 1):
            if i <= self.n // 2:
                print(i * '*')
            else:
                print((self.n + 1 - i) * '*')

p1=Piramis(5)
p2=Piramis(15)
p1.epit()
p2.epit()