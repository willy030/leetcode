#657
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        if moves.count("U")==moves.count("D") and moves.count("R")==moves.count("L"):
            return True
        return False
            

s=Solution()
print(s.judgeCircle("LL"))

