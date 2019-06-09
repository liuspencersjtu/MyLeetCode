class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text = text.split()
        res = []
        #print(text)
        for i in range(2,len(text)):
            #print(text[i-2],text[i-1],text[i])
            if text[i-1] == second and text[i-2]==first:
                res.append(text[i])
        return res
