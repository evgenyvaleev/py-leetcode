class Solution:
    def countAndSay(self, n: int) -> str:
        def read(n):
            if n == 1:
                return '1'
            else:
                s = read(n - 1)
                
                curr, cnt = s[0], 1
                res = ''
                for i in range(1, len(s)):
                    if s[i] == curr:
                        cnt += 1
                    else:
                        res += str(cnt) + curr
                        curr = s[i]
                        cnt = 1
                        
                res += str(cnt) + curr
                return res
            
        return read(n)          
        