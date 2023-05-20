class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        t = 0
        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[i] , nums[t] = nums[t] , nums[i]
                t +=1
                
        