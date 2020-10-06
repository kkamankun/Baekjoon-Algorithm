n = int(input())

for i in range(0, n):
  # map을 사용하여 정수로 변환하기
  x, y = map(int, input().split())
  result = int(x + y)
  print(result)
