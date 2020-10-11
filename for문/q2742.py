n = reversed(range(1, int(input()) + 1)) // 숫자를 감소시키기
print('\n'.join(map(str, n)))

# 다른 풀이
n = range(int(input()), 0, -1)
print("\n".join(map(str,n)))
