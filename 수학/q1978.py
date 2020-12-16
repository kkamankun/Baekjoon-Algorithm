def prime_number(number):
    if number != 1:
        for f in range(2, number):
            if number % f == 0:
                return False
    else:
        return False
    return True


N = int(input())
L = list(map(int, input().split()))
cnt = 0
for i in range(N):
    if prime_number(L[i]):
        cnt += 1
print(cnt)
