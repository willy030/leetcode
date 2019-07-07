#728
class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result=[]
        for i in range(left,right+1):
            j=str(i)
            re=1
            for k in j:
                if k!='0':
                    if i%int(k)!=0:
                        re=0
                        break
                else:
                    re=0
            if re==1:
                result.append(i)
        return result

s=Solution()
print(s.selfDividingNumbers(1,22))
