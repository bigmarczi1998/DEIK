class MyList(list):
    # list osztaly orokli
    def __init__(self, p1):
        super().__init__(p1)

    def print_items_with_indices(self):
        # szamlalot tudja helyettesiteni
        # 2 ciklusvaltozo, elso szamlalo, masodik pedig osszeparostja az iteratorral
        # konyvtar, kulcs-ertek parok
        for idx, item in enumerate(self):
            print('{}.elem: {}'.format(idx, item))

    # felul definialas
    def append(self, p1):
        super().append(p1 + 5)


l1 = MyList([4, 21, 2])
l1.print_items_with_indices()
l1.append(5)
print(l1)
