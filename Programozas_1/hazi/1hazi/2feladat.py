def haromszog_szamitas(a,b,c):
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
        #Heron-keplet
        a,b,c=int(a),int(b),int(c)
        s=(a+b+c)/2
        T=(s*(s-a)*(s-b)*(s-c))**0.5
        print('A haromszog terulete:'.format(T))