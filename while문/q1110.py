# n을 문자열로 바꿔서 temp에 저장
n = int(input())
temp = str(n)
count = 0

while True:
  sum = 0
  for i in range(len(temp)):
      sum += int(temp[i])

  new = temp[len(temp)-1] + str(sum)[len(str(sum))-1]

  count += 1
  if n == int(new):
    break;

  temp = new

print(count)

# 다른 풀이
N = int(input())

a = new = cnt = b = 0
if 0 <= N <= 99:
    b = N
    while 1:
        a = b // 10 + b % 10
        new = 10 * (b % 10) + a % 10
        cnt += 1
        if new == N: break
        b = new

print(cnt)
