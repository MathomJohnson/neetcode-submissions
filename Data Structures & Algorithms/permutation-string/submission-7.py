class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        # build count dict for substring
        sub = {}
        for c in s1:
            sub[c] = sub.get(c, 0) + 1

        l, r = 0, 0
        window = {}
        # populate initial window
        window[s2[r]] = window.get(s2[r], 0) + 1
        for i in range(len(s1) - 1):
            r += 1
            window[s2[r]] = window.get(s2[r], 0) + 1

        while r < len(s2) - 1:

            if window == sub: return True

            window[s2[l]] -= 1
            if window[s2[l]] == 0:
                del window[s2[l]]
            l += 1
            r += 1
            window[s2[r]] = window.get(s2[r], 0) + 1

        if window == sub: return True
        return False