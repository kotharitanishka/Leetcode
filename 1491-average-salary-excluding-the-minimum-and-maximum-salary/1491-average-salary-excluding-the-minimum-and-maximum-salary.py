class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        tot = 0
        for i in range (1 , len(salary)-1):
            tot = tot + salary[i]
        avg = tot/(len(salary)-2)
        return avg