class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = (-2)**31
        
        sign = -1 if x < 0 else 1
        s = str(abs(x))
        rev = s[::-1]
        res = sign * int(rev)

        # check overflow
        if res < INT_MIN or res > INT_MAX:
            return 0
        
        return res