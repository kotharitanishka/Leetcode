class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums)-1
        print(n)
        nums.sort()
        print(nums)
        if nums[n] != n :
            return False 
        for i in range (0,n):
            if nums[i] != i+1 :
                return False
            if nums[i+1] - nums[i] != 1 :
                if i != n-1 :
                    return False
        return True
        
                
            
            
    
        
            
        