# a: 고정 비용
# b: 가변 비용
# c: 책정된 노트북 가격
# n: 판매 대수
import sys
a, b, c = map(int, sys.stdin.readline().split())
if c - b > 0:
    n = a // (c - b)
    print(n+1)
else:
    print('-1')
