import sys

n = int(sys.stdin.readline())
for i in range(1, n+1):
  print(' ' * (n - i), end = '')
  print('*' * i)

# 다른 풀이
import sys

n = int(sys.stdin.readline())
for i in range(1, n+1):
  print(' ' * (n - i) + '*' * i)
