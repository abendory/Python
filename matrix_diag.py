n = 3
amatrix = [[0 for x in range(n)] for x in range(n)] 
i = total1=total2 = 0
amatrix = [[1,3,5],[7,2,6],[9,4,8]]
i = 0
while i<n:
	total1 += amatrix[i][i]
	total2 += amatrix[n-1-i][i]
	i+=1
print abs(total1-total2)