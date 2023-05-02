class Solution:
    def arraySign(self, nums: List[int]) -> int:
        n = len(nums)
        n = 0
        z = 0
        ans = 0
        for i in nums:
            if (i < 0) :
                n = n + 1
            elif (i == 0):
                z = z + 1
        
        if (z !=0):
            ans = 0
        elif (n % 2 == 0):
            ans = 1
        elif(n %2 != 0):
            ans = -1
        
        print(ans)
        return(ans)
            
            
            
        
        