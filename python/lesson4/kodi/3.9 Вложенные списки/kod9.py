lst = [5.4, 6.7, 10.4]
digs = list(map(int, input().split()))
lst.append(digs)
print(lst)

lst = []
for _ in range(3):
    line = input().split()
    lst.append(line)
print(lst)

matrix = [list(map(int, input().split())) for _ in range(3)]
print(matrix[0][-1], matrix[1][-1], matrix[2][-1])


t = [["Скажи-ка", "дядя", "ведь", "не", "даром"],
     ["Я", "Python", "выучил", "с", "каналом"],
     ["Балакирев", "что", "раздавал?"]]

t = [["Скажи-ка", "дядя", "ведь", "не", "даром"],
     ["Я", "Python", "выучил", "с", "каналом"],
     ["Балакирев", "что", "раздавал?"]]

word = input()