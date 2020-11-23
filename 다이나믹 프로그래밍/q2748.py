# Fn = Fn-1 + Fn-2 (n ≥ 2)
n = int(input())

fibonacci = [0, 1, 1]

if n > 2:
    for i in range(3, n+1):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

print(fibonacci[n])
