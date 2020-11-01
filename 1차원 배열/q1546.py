# 1차원 배열 입력받기
n = int(input())
A = list(map(int, input().split()))
sum = 0
for i in range(n):
    sum += A[i] / max(A) * 100
print(sum / n)
