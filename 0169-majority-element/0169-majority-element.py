class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {} 
        m = 0
        maj = 0
        for num in nums:
            if num in d :
                d[num] += 1
            else:
                d[num] = 1
        
        m = max(d.values())
        for k , v in d.items() :
            if v == m :
                return k
            
        # return maj