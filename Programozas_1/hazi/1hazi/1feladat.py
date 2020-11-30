def haromszog_helyes(a,b,c):
    if ((a+b)>c) and ((a+c)>c) and ((b+c)>a):
        c=True
    else:
        c=False
    return c

while True:
    old=input('oldalak (vesszovel elvalasztva):')
    if old=='end':
        break
    else:
        a,b,c=old.split(',')
        print(haromszog_helyes(int(a),int(b),int(c)))