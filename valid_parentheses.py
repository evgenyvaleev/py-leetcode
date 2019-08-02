class Solution:
    def isValid(self, s: str) -> bool:
        pairs = { '(': ')', '{': '}', '[': ']'}
        openings = ['(', '{', '[']
        
        stack = []
        for bracket in s:           
            if bracket in openings:
                stack.append(bracket)
            else:
                if len(stack) == 0 or pairs[stack[-1]] != bracket:
                    return False
                else:
                    stack.pop()
        
        return len(stack) == 0