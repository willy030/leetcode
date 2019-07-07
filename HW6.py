#905
class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        result=[]
        tmp=[]
        for i in A:
            if i%2==0:
                result.append(i)
            else:
                tmp.append(i)
        for i in tmp:
            result.append(i)
        return result
s=Solution()
print(s.sortArrayByParity([3,1,2,4]))

