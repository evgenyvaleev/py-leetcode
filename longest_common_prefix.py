class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lengths = [len(x) for x in strs]
        min_length = min(lengths) if len(lengths) > 0 else 0
        
        common_prefix = ''
        for i in range(min_length):
            is_common = True
            for j in range(len(strs) - 1):
                if strs[j][i] != strs[j + 1][i]:
                    is_common = False
                    break
            
            if is_common:
                common_prefix += strs[0][i]
            else:
                break
                
        return common_prefix