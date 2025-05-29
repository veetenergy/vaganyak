s = 'Тема занятия "спецсимволы"'
print(s)


s = input()
s = s.replace(' ', '\\')
print(s)


s = input()
first_split = s.split(' ', 1)  

if len(first_split) == 2:
    
    rest = first_split[1].replace(' ', '"')
    result = first_split[0] + "'" + rest
else:
    result = s  

print(result)



path = r"C:\WINDOWS\System32\drivers\etc\hosts"
print(path)



word = input()
result = '"' + word + '"'
print(result)