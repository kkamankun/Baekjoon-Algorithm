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
