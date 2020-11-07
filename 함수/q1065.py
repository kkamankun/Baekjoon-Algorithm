def seq(n):
    cnt = 0
    for i in range(1, n + 1):
        if i < 100:
            cnt += 1
        else:
            if int(str(i)[1]) - int(str(i)[0]) == int(str(i)[2]) - int(str(i)[1]):
                cnt += 1
    return cnt


print(seq(int(input())))

# 다른 풀이
n = int(input())
cnt = 0
if n < 100:
    print(n)
else:
    for i in range(100, n+1):
        if i//100-i//10 % 10 == i//10 % 10-i % 10:
            cnt += 1
    print(99+cnt)
