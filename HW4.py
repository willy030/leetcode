#804
dict={"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--.."}
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        result=[]
        for i in words:
            tmp=""
            for j in i:
                tmp+=dict[j]
            result.append(tmp)
        return len(list(set(result)))
        
s=Solution()
words = ["gin", "zen", "gig", "msg"]
print(s.uniqueMorseRepresentations(words))