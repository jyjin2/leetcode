class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX, INT_MIN = 2**31 - 1, -2**31
        i, n = 0, len(s)

        # 1. skip whitespace
        while i < n and s[i] == " ":
            i += 1
        # if string empty after spaces
        if i == n:
            return 0
        
        # 2. check sign
        sign = 1
        if s[i] in ['-', '+']:
            sign = -1 if s[i] == '-' else 1
            i += 1
        
        # 3. read digits
        res = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])

            # check overflow
            if res > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            res = res * 10 + digit
            i += 1
        return sign * res