# parancssori argumentumok

# modulok sys

# tesztprogram
# terminalba futtatunk
# Run-Edit_Configuration- + -Add_New_Configuration
# import sys
# for arg in sys.argv:
#     print(arg)

# 1feladat
# elso lista elemei nincsenek benne
# import sys
# def list_feltoltes(args): #argumentumot kapja meg
#     list1=[]
#     list2=[]
#     num_1=0
#     for arg in args:
#         if arg=="L:":
#             num_1+=1
#         else:
#             if num_1==1: #elso listanal jarunk
#                 list1.append(arg)
#             elif num_1==2: #masodik listanal jarunk
#                 list2.append(arg)
#     return list1, list2
# list1, list2 = list_feltoltes(sys.argv[1:])
# # print(list1)
# # print(list2)
# res_list=[]
# for item in list1:
#     if item not in list2:
#         res_list.append(item)
# print(res_list)

# 2feladat
# parancssorba irom hogy 5 output.txt
# import sys
# def osszead_n_ig(args):
#     n=int(args[0])
#     file_name=args[1]
#     out_file=open(file_name,"w") #majd a parancssorban adjuk meg hogy outfile.txt
#     sum=0
#     for i in range(n+1):
#         if i !=n:
#             sum+=i
#             print("{}+".format(i),end="",file=out_file)
#         else:
#             sum+=i
#             print("{}={}".format(i,sum),end="",file=out_file)
#     out_file.close()
# osszead_n_ig(sys.argv[1:]) #0 nem kell, mert az az eleresi ut, minden utanni kell!!!!!

# 3feladat
# import sys
# def kiir_datum(args):
#     num=int(args[0])
#     file_name=args[1]
#     out_file=open(file_name,"w")
#
#     year=num//(60*60*24*365) #egesz osztas, hany egesz evunk van azt kapjuk meg
#     num=num%(60*60*24*365) #ebbe hany masodperc marad, amivel kesobb dolgozhatunk
#
#     month=num//(60*60*24*30) #atlagosan 30 nap egy honap
#     num=num%(60*60*24*30)
#
#     day=num//(60*60*24)
#     num=num%(60*60*24)
#
#     hour=num//(60*60)
#     num=num%(60*60)
#
#     minute=num//60
#     num=num%60
#
#     sec=num
#
#     print("The current date is {}. {}. {}. {}:{}:{}".format(year,month,day,hour,minute,sec), file=out_file)
#     out_file.close()
#
# kiir_datum(sys.argv[1:])

# #4feladat
# import sys
# def string_sum(arg):
#     sum = 0
#     tmp = ""
#     for ch in arg:
#         if ch.isdigit():  # akkor igaz ha  akarakter egy szam
#             tmp += ch  # igy a helyiertek info is megmarad
#         elif tmp:  # tmp nem szam de van mas ch
#             sum += int(tmp)
#             tmp = ""
#     if tmp: #van-e benne elem(ha true akkor folytatodik)
#         sum+=int(tmp)
#     print("{} string osszege: {}".format(arg,sum))
#
# string_sum(sys.argv[1]) #vigyazz a : ra

#5feladat
# import sys, random
# def sum_random(args):
#     n=int(args[0])
#     file_name=(args[1])
#     sum=0
#     out_file=open(file_name,"w")
#
#     for i in range(n):
#         num=random.randint(1,100)
#         sum+=num
#         print(num,file=out_file)
#     print("Szamok osszege: {}".format(sum),file=out_file)
#
#     out_file.close()
#
# sum_random(sys.argv[1:])