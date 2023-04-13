class Solution:
    def reverse(self, x: int) -> int:
        r = 0
        flag = 0
        if (x < 0):
            flag = 1
            x = -x
        while(x>0):
            d = x %10
            x=x//10
            r = r*10 + d
        if -2147483648 <= r <= 2147483647:
            if (flag == 0):
                return(r)
            else :
                return(-r)
        else:
            return 0