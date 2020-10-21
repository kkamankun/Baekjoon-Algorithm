# n개의 정수를 입력받아 출력하기
n, x = map(int, input().split())
A = list(map(int, input().split()))
for i in A:
  if(i < x):
    print(i, end=' ')
    
# 다른 풀이
n, x = map(int, input().split())
score = [i for i in input().split() if int(i) < x]
print(' '.join(score))
