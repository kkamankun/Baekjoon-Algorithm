a, b = map(int, input().split())
# b를 a로 바꾸는 연산의 최솟값을 계산
cnt = 0
while a < b:
    # print(b)
    if str(b)[-1] == '1':
        b = int(str(b)[:-1])
    elif b % 2 == 0:
        b = b // 2
    else:
        break
    cnt += 1

if a == b:
    print(cnt+1)
else:
    print(-1)
