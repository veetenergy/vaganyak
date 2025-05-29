lst = list(map(int, input().split()))
lst.append(lst[0] != lst[-1])
print(*lst)


cities = ["Москва", "Казань", "Ярославль"]
cities.insert(1, "Ульяновск")
print(*cities)


phone = input()
lst = list(phone)
lst.pop(0)            
lst[0] = '8'          
while '-' in lst:
    lst.remove('-')   
print("".join(lst))


name, patronymic, surname = input().split()
print(f"{surname} {name[0]}.{patronymic[0]}.")


numbers = list(map(int, input().split()))
numbers.sort()
print(*numbers[:3])



lst = list(map(int, input().split()))
last = lst.pop()
lst.append(last % 2 != 0)
print(*lst)

marks = list(map(int, input().split()))
print(marks.count(2))


lst = input().split()
lst.sort()
lst.pop(0)
print(*lst)