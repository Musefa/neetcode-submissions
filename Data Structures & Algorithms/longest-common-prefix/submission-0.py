class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        shortest_word = min(strs, key=len)

        for i in range(len(shortest_word)):
            actual_char = shortest_word[i]

            for word in strs:
                if word[i] != actual_char:
                    return prefix
                    
            prefix += actual_char

        return prefix



            