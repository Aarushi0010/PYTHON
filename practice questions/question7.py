matrix = [[11,12,13] , [14,15,16] , [17,18,19]]
print("original matrix : ")
for row in matrix:
    print(row)
print()
k = 2
col_element = []
k = k-1
for i in range(len(matrix)):
    element = matrix[i][k]
    col_element.append(element)
col_element = col_element[::-1]
for j in range(len(matrix)):
    matrix[j][k] = col_element[j]
print("reversed matrix : ")
for row in matrix:
    print(row)