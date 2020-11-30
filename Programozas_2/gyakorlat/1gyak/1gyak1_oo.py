import math


class HalmazHatarertekek:

    def __init__(self, list):
        self.s = set(list)

    def keres(self):
        self.minim = math.inf
        self.maxim = -math.inf

        for item in self.s:
            if item > self.maxim:
                self.maxim = item
            if item < self.minim:
                self.minim = item
        return self.minim, self.maxim


halmaz_1 = HalmazHatarertekek([21, 4, -3, 23, 45, -21])
halmaz_2 = HalmazHatarertekek([21, 4, 3, 2, 1])
halmaz_3 = HalmazHatarertekek([45, -21])

print(halmaz_3.keres())
