#!/usr/bin/python

# print("helou")
# wyraz=str(input())
# print (wyraz)
import re

licznik=0
for linia in file("lorem.txt"):
    if "Bash" in linia:
        licznik=licznik+1
print"slowo Bash  ",licznik
reg_e='[0-9]'
licznik1=0
for linia in file("lorem.txt"):
    licznik1=licznik1+1
    if re.search(reg_e,linia):
        print"w linii", licznik1,"jest cyfra"

def czy_jest_cyfra_w_linii(nr):
    reg_f='[0-9]'
    licznik2=0
    for lin in file("lorem.txt"):
        licznik2=licznik2+1
        if licznik2==nr:
            if re.search(reg_f,lin):
                print"tak"
            else: print"nie"
    return(len(lin))

v=input("numer linii")
czy_jest_cyfra_w_linii(v)


