#832
class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in A:
            i.reverse()
            for j in range(0,len(i)):
                if i[j]==1:
                    i[j]-=1
                else:
                    i[j]+=1
        return A


s=Solution()

print(s.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))