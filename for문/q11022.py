n = int(input())

for i in range(0, n):
  x, y = map(int, input().split())
  print("Case #%d: %d + %d = %d"%(i+1, x, y, x+y))
  
# 다른 풀이
import sys
n = int(input())

for n in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(f'Case #{n+1}: {a} + {b} = {a+b}')
