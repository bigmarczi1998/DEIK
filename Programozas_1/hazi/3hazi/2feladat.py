import sys, random
def random_szam_listaban(args):
    n=int(args[0])
    file_name=args[1]
    list_one=[]
    list_two=[]
    list_result=[]
    out_file=open(file_name,"w")

    for i in range(n):
        num_one=random.randint(0,10)
        list_one.append(num_one)
    print('Első lista:',*list_one,sep=" ",file=out_file)

    for i in range(n):
        num_two=random.randint(0,10)
        list_two.append(num_two)
    print('Második lista:',*list_two,sep=" ",file=out_file)

    list_two.reverse()
    index_helye=0
    for i in list_one:
        x=i*list_two[index_helye]
        list_result.append(x)
        index_helye+=1
    print("Eredmény:",*list_result,sep=" ",file=out_file)

    out_file.close()

random_szam_listaban(sys.argv[1:])