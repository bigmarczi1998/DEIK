import sys
def anagramma(args):
    first_str=args[0]
    second_str=args[1]

    a=[]
    for i in range(len(first_str)- 1,-1,-1):
        a.append(first_str[i])
    print(a)

    b=[]
    for i in range(len(second_str)):
        b.append(second_str[i])
    print(b)

    if a==b:
        print('Igaz')
    else:
        print('Hamis')

anagramma(sys.argv[1:])