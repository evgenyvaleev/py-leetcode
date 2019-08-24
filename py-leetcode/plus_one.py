from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        shift = 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i] = digits[i] + shift
            if digits[i] > 9:
                digits[i] -= 10
                shift = 1
            else:
                shift = 0
        
        if shift > 0:
            digits = [shift] + digits
        
        return digits
