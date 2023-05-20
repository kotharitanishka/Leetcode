class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {} 
        m = 0
        maj = 0
        for num in nums:
            if num in d :
                d[num] +=1
            else:
                d[num] = 1
        
        for k , v in d.items() :
            if v > m:
                m = v
                maj = k
            
        return maj