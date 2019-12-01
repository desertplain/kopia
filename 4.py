#!/usr/bin/python

print("helou")
wyraz=input("podaj wyra :   ")
print wyraz
licznik=0
for linia in file("lorem.txt"):
    if "Bash" in linia:
        licznik=licznik+1
print"slowo Bash  ",licznik
