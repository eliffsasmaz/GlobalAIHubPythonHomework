# -*- coding: utf-8 -*-
"""

@author: eliffsasmaz
"""



first_name=input('Please Enter Your Name:')
last_name=input('Please Enter Your Surname:')
age=int(input('Please Enter Your Age :'))
year_of_birth=int(input('Please Enter the Year that You Born:'))

user_info=[first_name,last_name,age,year_of_birth]

for i in range(4):
    
    print(user_info[i])
    

check=2020-user_info[3]


if user_info[2]==check:
    if user_info[2] <18: 
        print('You Should Not Go Out,Because It is too Dangerous!!')
    else:
        print('You can go out to the street.')
else:
    print('age and year are not match!')
    
    
    
    

