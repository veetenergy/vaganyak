
s = input()
print(s[0] + s[-1])


s = input()
print(s[:4])


s = input()
print(s[-3:])


s = input()
print(s[1::2])



s1 = input()
s2 = input()
result = s1[0::2] + ' ' + s2[1::2]
print(result)



s = input()
print(s[:5][::-1])




s = input().split()
first, second = s[0], s[1]
print(second[:len(first)])



s = input().split()
first, second = s[0], s[1]
first = first[:len(second)]
print(first[1::2] == second[1::2])