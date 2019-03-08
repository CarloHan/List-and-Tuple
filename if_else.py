# -*- coding: utf-8 -*-

'''
age = 20
if age >= 18:
    print('your age is', age)
    print('adult')

age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
elif age >=6:
    print("your age is", age)
    print('teenager')
else:
    print('your age is', age)
    print('kid')


s = input('bitrh: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')
'''

h = input('Please input your height(m): ')
height = float(h)
w = input('Please input your weight(kg): ')
weight = float(w)

bmi = weight / height ** 2
print('BMI = ', bmi)

if bmi > 32:
    print('严重肥胖！')
elif bmi > 28:
    print('肥胖')
elif bmi > 25:
    print('过重')
elif bmi > 18.5:
    print('正常')
else:
    print('过轻！')
