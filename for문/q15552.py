# 입출력 방식이 느리면 여러 줄을 입력받거나 출력할 때 시간초과가 날 수 있다.
# input 대신 sys.stdin.readline을 사용할 수 있다.
import sys

n = int(sys.stdin.readline())

for i in range(0, n):
  x, y = map(int, sys.stdin.readline().split())
  result = int(x + y)
  print(result)
