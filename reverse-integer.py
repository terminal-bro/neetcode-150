class Solution:
    def reverse(self, x: int) -> int:
        reverse = 0
        rem = 0
        sign = 1 if x >= 0 else -1
        x = abs(x)

        while x > 0:
            rem = x % 10
            reverse = reverse*10 + rem
            x = x//10

        if reverse > 2**31-1:
            return 0
        return reverse*sign