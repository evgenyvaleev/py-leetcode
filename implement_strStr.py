class Solution1:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        
        h_pos = 0
        n_pos = 0
        catch_pos = -1
        while h_pos < len(haystack):
            if haystack[h_pos] == needle[n_pos]:
                if catch_pos == -1:
                    catch_pos = h_pos
                
                if n_pos == len(needle) - 1:
                    return catch_pos
                    
                h_pos += 1
                n_pos += 1
            elif catch_pos != -1:
                h_pos = catch_pos + 1
                n_pos = 0
                catch_pos = -1
            else:
                h_pos += 1
                
        if catch_pos != -1 and n_pos != len(needle):
            return -1
                        
        return catch_pos

class Solution2:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        
        for i in range(len(haystack) - (len(needle) - 1)):
            if haystack[i:i+len(needle)] == needle:
                return i
                          
        return -1
