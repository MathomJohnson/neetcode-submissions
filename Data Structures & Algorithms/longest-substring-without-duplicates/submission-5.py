class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        res = 0
        l, r = 0, 0
        window = set()

        while r < len(s):

            if s[r] in window: # shorten window from left
                while s[l] != s[r]:
                    window.remove(s[l])
                    l += 1
                l += 1

            window.add(s[r])
            res = max(res, r - l + 1)
            r += 1

        return res

            