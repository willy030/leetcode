#461
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        result=[]
        result.append(bin(x)[2:][::-1])
        result.append(bin(y)[2:][::-1])
        if len(result[0])>len(result[1]):
            mm=len(result[0])-len(result[1])
            for i in range(0,mm):
                result[1]+="0"
        else:
            mm=len(result[1])-len(result[0])
            for i in range(0,mm):
                 result[0]+="0"
        count=0
        i=0
        while i!=len(result[0]):
            if result[0][i]!=result[1][i]:
                count+=1
            i+=1
              
        return count
        
s=Solution()
print(s.hammingDistance(1,4))
