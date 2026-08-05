class Solution:
	def firstAlphabet(self, s):
		# code here
		l = s.split()
		res = ""
		for word in l:
		    res += word[0]
		return res