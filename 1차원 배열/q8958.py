n = int(input())
A = [input() for _ in range(n)]

for i in range(n):
    cnt = 0
    sum = 0
    for j in range(len(A[i])):
        if (A[i][j] == 'o'):
            cnt += 1
            sum += cnt
        else:
            cnt = 0
    print(sum)
    
# 다른 풀이
import sys

n = int(input())
for i in range(n):
    A = sys.stdin.readline().rstrip()
    res = 0
    for j in A.split('X'):
        k = j.count('O')
        res += k*(k+1)/2

    print(int(res))
