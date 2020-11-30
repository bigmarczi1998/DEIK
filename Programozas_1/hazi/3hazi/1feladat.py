import sys
def szavak_sorrend(args):
    list_one=[]
    list_two=[]
    n_hossz=int(args[0])
    for i in args:
        if i.isdigit():
            continue
        if len(i)<n_hossz:
            list_one.append(i)
        elif len(i)>n_hossz:
            list_two.append(i)
    print("list1 = {}".format(list_one))
    print("list2 = {}".format(list_two))

szavak_sorrend(sys.argv[1:])