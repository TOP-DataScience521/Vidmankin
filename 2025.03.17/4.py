try:
    n = int(input('Введите число:'))
    
except ValueError:  
    print('Не является числом')

except NameError:
    print('Не является числом')

else:
    if n > 0 and (n & (n - 1)) == 0:
        print ('да')
    else:    
        print('нет')


# Введите число:1
# да


# Введите число: -8
# нет


# Введите число:1
# да


# Введите число:dgdsg
# Не является числом


