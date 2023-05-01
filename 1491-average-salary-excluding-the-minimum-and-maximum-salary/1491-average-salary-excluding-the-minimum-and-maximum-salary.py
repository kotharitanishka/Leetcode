class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        del salary[0]
        del salary[-1]
        tot = 0
        for i in range (0 , len(salary)):
            tot = tot + salary[i]
            print(tot)
        avg = tot/len(salary)
        print(salary)
        print(avg)
        return avg