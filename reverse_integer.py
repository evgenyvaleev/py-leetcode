class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x < 0
        x = abs(x)

        reversed_str = str(x)[::-1]
        reversed_int = int(reversed_str)
        if is_negative:
            reversed_int *= -1

        if reversed_int < (-2 ** 31) or reversed_int > (2 ** 31 - 1):
            return 0

        return reversed_int
