class Solution:
    def romanToInt(self, s: str) -> int:
        mappings = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        subtract_before = {'I': ['V', 'X'], 'X': ['L', 'C'], 'C': ['D', 'M']}
        
        res = 0
        last = None
        for symbol in s[::-1]:
            if symbol in subtract_before and last in subtract_before[symbol]:
                res -= mappings[symbol]
            else:
                res += mappings[symbol]
                
            last = symbol
                
        return res
