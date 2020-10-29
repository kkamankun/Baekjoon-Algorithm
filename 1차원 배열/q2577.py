x = int(input())
y = int(input())
z = int(input())

result = x * y * z
A = list(map(int, list(str(result))))
print(A.count(0))
print(A.count(1))
print(A.count(2))
print(A.count(3))
print(A.count(4))
print(A.count(5))
print(A.count(6))
print(A.count(7))
print(A.count(8))
print(A.count(9))

# 다른 풀이
x = int(input())
y = int(input())
z = int(input())

for i in range(10):
    print(str(x * y * z).count(str(i)))
