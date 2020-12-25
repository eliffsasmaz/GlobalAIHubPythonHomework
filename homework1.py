# -*- coding: utf-8 -*-
"""

@author: eliffsasmaz
"""

#Assume that user enters valid values to program.

values=[]

values.append(int(input('Please enter a positive integer:')))
values.append(int(input('Please enter a negative integer:')))
values.append(float(input('Please enter a float number between 0 and 10 :')))
values.append(float(input('Please enter a different float number:')))
values.append(float(input('Please enter a negative float number:')))

print(f'a positive {type(values[0]),values[0]}')
print(f' a negative {type(values[1]),values[1]}')
print(" a float number between 0 and 10 :{}".format(type(values[2])),values[2])
print(" a number which is :{}".format(type(values[3])),values[3])
print(" a negative number which is :{}".format(type(values[4])),values[4])
