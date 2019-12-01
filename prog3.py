#!/usr/bin/python3

z=0
y=[]
for i in range(2000,3000+1,1):
    if i%7==0 and i%5!=0:
        y.append(i)
        z=z+1
print(y)
print(z)
