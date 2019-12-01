#!/usr/bin/python3

x=input('liczba: \n')
y=x.split(",")
for i in range(len(y)):
    y[i]=int(y[i])
print(y)

