class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs.sort()
        first_str= strs[0]
        last_str=strs[-1]
        prefix=""

        rang=min(len(first_str),len(last_str))
        for i in range(rang):
            if first_str[i] == last_str[i]:
                prefix += (first_str[i])
            else:
                break
        
        return prefix
