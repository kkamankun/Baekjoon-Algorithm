# LCS
str1 = input().strip().upper()
str2 = input().strip().upper()
matrix = [[0 for col in range(len(str2)+1)] for row in range(len(str1)+1)]
for i in range(1, len(str1)+1):
    for j in range(1, len(str2)+1):
        if str1[i-1] == str2[j-1]:
            matrix[i][j] = matrix[i-1][j-1] + 1
        else:
            matrix[i][j] = max(matrix[i][j-1], matrix[i-1][j])

# for i in matrix:
#     for j in i:
#         print(j, end=" ")
#     print()

print(matrix[-1][-1])
