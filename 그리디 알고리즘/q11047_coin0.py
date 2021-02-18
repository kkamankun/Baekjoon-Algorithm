# 그리디 알고리즘:
# 가장 큰 동전 단위부터 필요한 동전의 개수를 센다.
n, k = map(int, input().split())
lst = []
cnt = 0

for i in range(n):
    lst.append(int(input()))

lst.sort(reverse=True)
for i in lst:
    cnt += k//i
    k %= i

print(cnt)
