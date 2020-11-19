# 숫자의 합
n = int(input())
s = input()
t = 0
for i in range(len(s)):
    t += int(s[i])
print(t)

# 여러 개의 데이터를 한번에 다른 형태로 변환하는 map()
n = int(input())
s = map(int, input())
print(sum(s))
