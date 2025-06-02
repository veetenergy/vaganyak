#№1
a, b = map(float, input().split())

if a > b:
    print(a)
else:
    print(b)
#№2
word = input().lower()

if word == word[::-1]:
    print("ДА")
else:
    print("НЕТ")
#№3
m, n = map(int, input().split())

if m % n == 0:
    print(m // n)
else:
    print(f"{m} на {n} нацело не делится")
#№4
a, b, c = map(int, input().split())

if a**2 + b**2 == c**2:
    print("ДА")
else:
    print("НЕТ")
#№5
num = input()

if num[-1] == '7':
    print("ДА")
else:
    print("НЕТ")

#№6
s = input().lower()

if 't' in s and 'h' in s and 'o' in s:
    print("ДА")
else:
    print("НЕТ")
#№7
cities = input().split()

if "Москва" in cities:
    cities.remove("Москва")

print(*cities)
#№8
a, b, c, d = map(int, input().split())


w, h = a - 2, b - 2


if (c <= w and d <= h) or (d <= w and c <= h):
    print("ДА")
else:
    print("НЕТ")
#№9
num = input()

first_sum = int(num[0]) + int(num[1]) + int(num[2])
second_sum = int(num[3]) + int(num[4]) + int(num[5])

if first_sum == second_sum:
    print("ДА")
else:
    print("НЕТ")

#№10
t = float(input())
cycle = t % 5  

if cycle < 3:
    print("green")
else:
    print("red")

