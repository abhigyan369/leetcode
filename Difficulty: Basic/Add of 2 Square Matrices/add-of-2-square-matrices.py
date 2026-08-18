class Solution:
	def addMat(self, a, b):
		# Code here
		n = len(a)
		m = len(a[0])
		c = [[0]*m for _ in range(n)]
		for i in range(n):
		    for j in range(m):
		        #c[i][j] = a[i][j] + b[i][j]
		        a[i][j] += b[i][j]
		return a