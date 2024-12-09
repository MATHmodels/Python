L = [[9, 7], [1, 5, 6]]
for i in range(len(L)):
    for j in range(len(L[i])):
        print(L[i][j], end=' ')

print()

for row in L:
    for column in row:
        print(column, end=' ')
