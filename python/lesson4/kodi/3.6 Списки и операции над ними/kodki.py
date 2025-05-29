lst = list(map(int, input().split()))
print(lst)



cities = input().split()
print("Москва" in cities)


cities = input().split()
print(cities[-1])


marks = list(map(int, input().split()))
average = sum(marks) / len(marks)
print(f"{average:.1f}")


title = input()
author = input()
pages = int(input())
price = float(input())

book = [title, author, pages, price]


del book[2]


book[1] = "Пушкин"


book[2] *= 2

print(book)



subs = list(map(int, input().split()))
print(max(subs), min(subs), sum(subs))



lst = list(map(int, input().split()))
lst.sort(reverse=True)
print(*lst)


cities = ["Москва", "Тверь", "Вологда"]
lst = cities + input().split()
print(*lst)



cities = ["Москва", "Тверь", "Вологда"]
lst = input().split() + cities
print(*lst)