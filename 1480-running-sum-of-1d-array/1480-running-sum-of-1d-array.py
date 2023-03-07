class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        i = 0
        j = 0
        for num in nums :
          j = j + num
          nums[i] = j
          i = i + 1
        return(nums)