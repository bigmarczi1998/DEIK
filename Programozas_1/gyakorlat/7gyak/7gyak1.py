

dict = {"Bob":"dog","Kitty":"cat","Edward":"fish"}

for key in dict.keys():
    print("{} is a {}".format(key,dict[key]))


#marcsi
import sys
'''
Hozzon létre egy szótárat, amely állatokról tartalmaz információt!
A kulcs az állat neve és a hozzá tartozó érték az állat fajtája.
Például:
"Ziggy":"canary"
Tegyen legalább 3 kulcs-érték párt a szótárba!
Egy for ciklussal járja be a szótárat és írassa ki minden állat nevét és fajtáját a követ-
kező formátumban:
"Ziggy is a canary."
'''
def main():
    d = {}
    d["Ziggy"] = "canary"
    d["Tom"] = "cat"
    d["Willie"] = "dog"

    for k in d.keys():
        print('{} is a {}.'.format(k,d[k]))

    for k in d.keys():
        print(k)


    dictionary = {
        "x":5,
        "y":10,
        "z":25
    }
    print(dictionary["x"])

if __name__ == '__main__':
    main()