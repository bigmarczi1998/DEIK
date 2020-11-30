n = int(input("Kerek egy szamot(sorok): "))
for i in range(1, n + 1):
    if i <= n // 2:
        print(i * '*')
    else:
        print((n + 1 - i) * '*')
