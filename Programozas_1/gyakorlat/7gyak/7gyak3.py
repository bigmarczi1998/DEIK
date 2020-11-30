

def convert_date(datum):
    datum_dict = {}
    list = ['JAN','FEB','MAR','APR','MAY','JUN'\
            ,'JUL','AUG','SEP','OCT','NOV','DEC']
    num = 1
    for month in list:
        datum_dict[month] = num
        num += 1
    datum_list = datum.split('-')
    day = int(datum_list[0])
    month = datum_dict[datum_list[1]]
    if int(datum_list[2]) > 20:
        year = 1900 + int(datum_list[2])
    else:
        year = 2000 + int(datum_list[2])
    return (year, month, day)

datum = input("Kerem a datumot: ")
converted_date = convert_date(datum)
print(converted_date)



#marcsi
import sys

'''
Írjon függvényt, amely egy paraméterként átadott sztringet, (ami egy dátumot reprezentál a következő 
formátumban: dd-MMM-yy), átkonvertálja a következő formátumba: (yyyy,mm,dd).

Tegyük fel, hogy csak 1920 és 2019 közötti évszámok lehetségesek!

pl.: bemenet: "8-MAR-85"
     kimenet: ('1985','03','08')
'''


def convertDate(date):
   parts = date.split('-')
   print(parts)
   year = ''
   if int(parts[2]) < 20:
       year = '20'+parts[2]
   else:
       year = '19'+parts[2]

   months_names = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
   months_nums = list(range(1,13))
   months_dict = dict(zip(months_names, months_nums))

   if months_dict[parts[1]] < 10: #months_dict['DEC'] = 12
       month = '0'+ str(months_dict[parts[1]])
   else:
       month = str(months_dict[parts[1]])

   if int(parts[0]) < 10:
       day = '0'+parts[0]
   else:
       day = parts[0]

   return (year, month, day)


def main():
    (y,m,d) = convertDate("15-DEC-25")
    print(y)
    print(m)
    print(d)
if __name__ == "__main__":
    main()