def binomial_coefficient(n):
	bc = [[0 for x in range(n+1)] for y in range(n+1)]

	for i in range(n+1):
		bc[i][0] = 1
	for j in range(n+1):
		bc[j][j] = 1

	for i in range(n+1):
		for j in range(1,i):
			bc[i][j] = bc[i-1][j-1] + bc[i-1][j]
	return bc[n]

print binomial_coefficient(10)
	