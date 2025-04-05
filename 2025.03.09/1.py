from datetime import datetime


# Ввод данных
name = input("Введите Ваше Имя: ")
suname = input("Введите Вашу Фамилию:")
age = input("Введите свой год рождения:")
var1 = int(age)

# запрос текущей даты
nowyear = datetime.now().year
var2 = int(nowyear)
year = var2 - var1

print(suname, name, f', {year}')


# Введите Ваше Имя: Юрий
# Введите Вашу Фамилию:Видманкин
# Введите свой год рождения:1976
# Видманкин Юрий , 49

