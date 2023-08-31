 # Typecasting: conversion of one datatype into another datatype
# Two types of typecasting 1) Explicit -> Programmer will change code according to their need by using int(),float() etc. 2)Implicit means Pyhton understand the logic of the code and change that according to their own.

# Explicit Typecasting
a='3'
b='1'

print('values is:', type(a+b))
print('\nvalues is:', a+b)

# int
print('int is:', int(a)+int(b))
# Float
print('Float is:', float(a)+float(b))

#Implicit Typecasting

c=3.6
d=1
print('\n\n\nvalues is:', type(c+d))
print('\nvalues is:', c+d)

