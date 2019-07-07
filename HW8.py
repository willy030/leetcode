#1021
class Solution(object):
    def removeOuterParentheses(self,S):
        result=""
        tmp=""
        countL=0
        countR=0
        for i in S:
            if i=='(':
                countL+=1
                if countL!=1:
                    tmp+=i
            elif i==')':
                countR+=1
                if countL!=countR:
                    tmp+=i
            if countL==countR and countL>0:
                result+=tmp
                countL=0
                countR=0
                tmp=""
            
        return result

s=Solution()
print(s.removeOuterParentheses("(()())(())(()(()))"))

