#!/usr/bin/python3
def silnia_n_1(n):
    if n>1:
        return n*silnia_n_1(n-1)
    elif n in (0,1):
        return 1
x=int(input("podaj liczbe: \n"))
print(silnia_n_1(x))

