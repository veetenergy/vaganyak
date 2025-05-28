
word = input()
print(word.capitalize())



s = input()
print(s.count('-'))


s = input()
print(s.find("ra"))



s = input()

s = s.replace('---', '-')

s = s.replace('--', '-')
print(s)


a, b, c = map(int, input().split())
print(f"{a:03d}")
print(f"{b:03d}")
print(f"{c:03d}")


s = input()
words = s.split()
print(len(words))


cities = input().split()
print(';'.join(cities))