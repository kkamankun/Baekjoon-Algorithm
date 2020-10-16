a = int(input())
x = input()
digit = 1
result = 0
for i in reversed (x):
    print (a*int(i))
    result = result + (a*int(i))*digit
    digit = digit * 10
print(result)
