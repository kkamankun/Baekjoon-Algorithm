def sum_digit(number):
    result = number
    for i in str(number):
        result = result + int(i)
    return result


A = [i for i in range(10000)]

for i in range(10000):
    item = sum_digit(i)
    if item in A:
        A.remove(item)

for i in A:
    print(i)
