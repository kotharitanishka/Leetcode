class Solution:
    def average(self, salary: List[int]) -> float:
        tot = 0
        for i in range (0 , len(salary)):
            tot = tot + salary[i]
        tot = tot - max(salary) - min(salary)
        avg = tot/(len(salary)-2)
        return avg