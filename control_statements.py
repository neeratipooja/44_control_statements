'''
DAY:saturday
DATE:3rd  dec 2022
TOPIC:control statements
AUTHOR:pooja
'''
a=int(input('enter the value of a:'))
if(a==5):
  print("equal")#5(value) then it print equal
  print('equal') #3(value) it dosnot print anything
a,b=(int(x) for x in input().split())
if(a<b): #5<3
  print('a is less than b')
else:
  print('a is equal to b')  # a is equal to b
a,b=(int(x) for x in input().split()) #8 6
if(a>b):print('a is greater then b')# a is > than b
if(a<b):print('a is less than b')
if(a>=b):print('a is greater than or equal to b')#a is >= b
if(a<=b):print('a is less than or equal to b')
if(a!=b):print('a is not equal to b')# a is != b
if(a==b):print('a is equal to b')  