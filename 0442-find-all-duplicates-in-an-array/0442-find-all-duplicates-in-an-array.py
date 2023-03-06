class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = Counter(nums)
        num = []
        for key , v in n.items():
            if v == 2 :
                num.append(key)
        return(num)