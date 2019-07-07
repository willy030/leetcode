#977
class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        for i in range(0,len(A)):
            A[i]=A[i]**2
        A=sorted(A)
        return A
        
        
s=Solution()
print(s.sortedSquares([-4,-1,0,3,10]))
