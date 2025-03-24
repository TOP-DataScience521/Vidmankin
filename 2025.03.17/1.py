from decimal import Decimal

num1 = input('число 1: ')
num2 = input('число 2: ')
num3 = input('число 3: ')

num1 = Decimal(num1)
num2 = Decimal(num2)
num3 = Decimal(num3)


if num1>0:
    num_1=num1
elif num1<=0:
     num_1=0
if num2>0:
    num_2=num2
elif num2<=0:
     num_2=0
if num3>0:
    num_3=num3
elif num3<=0:
     num_3=0         

sum=num_1+num_2+num_3


print ("сумма положительных чисел", sum)


#число 1: 4
#число 2: -22
#число 3: 1.5
#сумма положительных чисел 5.5
    