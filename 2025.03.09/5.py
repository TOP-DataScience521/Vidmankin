mil = input('Введите целое число миль:')
yard = input('Введите число после запятой:')
a = (int(mil) + int(yard)*0.1) * 1.61
km = round(a, 1)
print(f'{mil}.{yard} миль = {km} км')


# Введите целое число миль:28
# Введите число после запятой:23
# 28.23 миль = 48.8 км

