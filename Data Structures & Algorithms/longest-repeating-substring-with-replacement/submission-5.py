class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        res = k
        window = {} # key: char, val: count
        l, r = 0, 0

        # populate initial window
        window[s[r]] = window.get(s[r], 0) + 1
        for i in range(k-1):
            r += 1
            window[s[r]] = window.get(s[r], 0) + 1

        while r < len(s):

            curr = -1 # holds count of most common char
            for val in window.values():
                curr = max(curr, val)

            gap = (r - l + 1) - curr

            if k >= gap:
                res = max(res, r - l + 1)
                r += 1
                if r < len(s): 
                    window[s[r]] = window.get(s[r], 0) + 1

            else:
                window[s[l]] -= 1
                l += 1

        return res
