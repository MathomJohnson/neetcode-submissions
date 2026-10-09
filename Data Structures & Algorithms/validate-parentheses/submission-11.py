class Solution:
    def isValid(self, s: str) -> bool:
        
        opened = set(['(', '[', '{'])
        closed = set([')', ']', '}'])

        matches = {'(': ')',
                    '[': ']',
                    '{': '}'}

        stack = []

        for c in s:

            if c in closed:
                if not stack: return False
                else:
                    p = stack.pop()
                    if matches[p] != c: return False

            if c in opened:
                stack.append(c)

        if stack: return False
        return True