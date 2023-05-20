class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq = [0] * 26
        for i in range(len(s)):
            freq[ord(s[i]) - ord('a')] += 1
            freq[ord(t[i]) - ord('a')] -= 1
        
        for i in range(len(freq)):
            if freq[i] != 0:
                return False
        
        return True

    
        # s1 = list(s)
        # s2 = list(t)
        # s1.sort()
        # s2.sort()
        # if(s1 == s2):
        #     return(True)
        # else :
        #     return(False)