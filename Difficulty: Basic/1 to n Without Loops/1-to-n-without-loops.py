class Solution:
    def pr(self,index,n):
        if index > n:
            return
        print(index, end=" ")
        self.pr(index+1,n)
    def printTillN(self, n):
    	#code here 
    	self.pr(1,n)