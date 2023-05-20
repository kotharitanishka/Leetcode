class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = 0
        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[i] , nums[n] = nums[n] , nums[i]
                n +=1
                
        