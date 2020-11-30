import string

def count_words(my_file):
    dict = {}
    for line in my_file:
        new_line = ""
        for ch in line:
            if ch not in string.punctuation:
                new_line += ch
        words = new_line.split()
        for word in words:
            if word in dict:
                dict[word] += 1
            else:
                dict[word] = 1
    return dict

my_file = open("input.txt","r")
dict = count_words(my_file)
for key,value in dict.items():
    print("{} elofordulasainak szama: {}".format(key,value))
my_file.close()



#marcsi
import sys
import string
'''
Írjon függvényt, amely az input.txt-ben előforduló szavak gyakoriságát számolja meg. 
A feladat megoldásához szótárat használjon!
'''
def clearRow(row):
    new_row = ""
    for ch in row:
        if ch not in string.punctuation and ch != '\n':
            new_row += ch.lower()
    return new_row

def main():
    frequency = {}
    with open("input.txt", "r") as f:
        for row in f:
            row = clearRow(row)
            for word in row.split(' '):
                if word in frequency.keys():
                    frequency[word] += 1
                else:
                    frequency[word] = 1

    print(frequency)

if __name__ == "__main__":
    main()