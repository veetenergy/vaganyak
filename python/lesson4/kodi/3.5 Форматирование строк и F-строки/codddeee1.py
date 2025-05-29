name = input()
surname = input()
age = input()

result = "Уважаемый {} {}! Поздравляем Вас с {}-летием!".format(name, surname, age)
print(result)


w, d, h = input().split()

result = "Габариты: {ширина} x {глубина} x {высота}".format(ширина=w, глубина=d, высота=h)
print(result)


a, b = map(int, input().split())
x, y = sorted([a, b])
print(f"{x} {y}")



city = input()
street = input()
house = int(input())
apartment = int(input())

print(f"г. {city}, ул. {street}, д. {house}, кв. {apartment}")



course = float(input())
rub = int(input())

dollars = int(rub // course)

print(f"Вы можете получить {dollars}$ за {rub} рублей по курсу {course}")