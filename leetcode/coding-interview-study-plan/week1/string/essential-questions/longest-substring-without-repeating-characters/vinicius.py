'''
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # OLDER
        # if len(s) == 0:
        #     return 0
        # if len(s) == 1:
        #     return 1
        # substr = ''
        # max_len = 1
        # for i in range(0,len(s)):
        #     substr = s[i]
        #     j = i+1
        #     while j < len(s) and s[j] not in substr:
        #         substr += s[j]
        #         j+=1
        #     if len(substr) > max_len:
        #         max_len = len(substr)
        # if len(substr) > max_len:
        #     max_len = len(substr)
        # return max_len
        
        if len(s) == 0 or len(s) == 1:
            return len(s)
        seen = []
        max_subst = 0
        end = 0
        for i in range(len(s)):
            if s[i] not in seen: #Se o valor não é repetido
                seen.append(s[i])
                max_subst = max(max_subst, len(seen))
            else: #Se é repetido
                seen.append(s[i]) #Primeiro adiciona o valor repetido
                while end < len(s) and len(set(seen)) != len(seen): #Vai retirando e movendo a janela do end enquanto o end < len(s) e até ficar sem elementos repetidos
                    seen.remove(s[end])
                    end +=1
        return max_subst