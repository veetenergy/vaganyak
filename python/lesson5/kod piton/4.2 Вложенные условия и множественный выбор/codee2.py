#№1
m = '''1. Введение в Python
2. Строки и списки
3. Условные операторы
4. Циклы
5. Словари, кортежи и множества
6. Выход'''

# Разбиваем меню на список строк
menu = m.split('\n')

# Считываем число
n = int(input())

# Используем if-elif для выбора пункта
if n == 1:
    print(menu[0])
elif n == 2:
    print(menu[1])
elif n == 3:
    print(menu[2])
elif n == 4:
    print(menu[3])
elif n == 5:
    print(menu[4])
elif n == 6:
    print(menu[5])
#№2
a, b, c = map(int, input().split())


min_val = a

if b < min_val:
    min_val = b
if c < min_val:
    min_val = c

print(min_val)
#№3
weight = float(input())

if weight <= 60:
    print(1)
elif weight <= 64:
    print(2)
elif weight <= 69:
    print(3)
else:
    print(4)
#№4
day = int(input())

if day == 1:
    print("понедельник")
elif day == 2:
    print("вторник")
elif day == 3:
    print("среда")
elif day == 4:
    print("четверг")
elif day == 5:
    print("пятница")
elif day == 6:
    print("суббота")
elif day == 7:
    print("воскресенье")

#№5
month = int(input())

if month == 2:
    print(28)
elif month in [4, 6, 9, 11]:
    print(30)
else:
    print(31)
#№6
m, n = map(int, input().split())

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


if n > 1:
    prev_m, prev_n = m, n - 1
else:
    prev_m = m - 1
    prev_n = days_in_month[prev_m - 1]


if n < days_in_month[m - 1]:
    next_m, next_n = m, n + 1
else:
    next_m = m + 1
    next_n = 1

print(f"{prev_m:02}.{prev_n:02} {next_m:02}.{next_n:02}")

#№7
k = int(input())

days = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]


day_of_week = days[(k - 1) % 7]

print(day_of_week)
