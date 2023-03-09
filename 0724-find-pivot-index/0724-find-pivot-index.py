class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l,r = 0, sum(nums)
        for index, num in enumerate(nums):
            r-=num
            if l==r:
                return index
            l+=num
        
        return -1