a = 1
b = 1
while(a != 0 and b != 0):
  a, b = map(int, input().split())
  if(a != 0 and b != 0):
    print(int(a + b))
    
# 다른 풀이
import sys

while True:
	(a, b) = map(int, sys.stdin.readline().split())
	if (a == 0 and b == 0):
		break
	print(a+b)
