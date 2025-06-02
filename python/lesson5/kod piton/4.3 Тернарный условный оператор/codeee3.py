#№1
a = float(input())
b = float(input())

d = a if a > b else b

print(d)
#№2
n = int(input())

msg = "кратно 3" if n % 3 == 0 else "не кратно 3"

print(msg)

#№3
word = input()
msg = "палиндром" if word.lower() == word.lower()[::-1] else "не палиндром"
print(msg)
#№4
n = int(input())
result = "True" if n == 1 else "False"
print(result)
#№5
n = int(input())
next_sec = 0 if n == 59 else n + 1
print(next_sec)
#№6
m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
nums = list(map(int, input().split()))

result = ' '.join(('#' + m[i-1] if m[i-1] in ['до', 'фа'] else m[i-1]) for i in nums)
print(result)
