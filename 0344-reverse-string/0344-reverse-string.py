class Solution:
    def reverseString(self, s: List[str]) -> None:
        for j in range (len(s)):
            s.insert(j , s[-1])
            s.pop()
            j +=1