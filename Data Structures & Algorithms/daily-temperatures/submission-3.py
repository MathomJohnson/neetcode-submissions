class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):

            if not stack:
                stack.append([t, i])
                continue

            while stack and t > stack[-1][0]:
                p = stack.pop()
                res[p[1]] = i - p[1]
            
            stack.append([t, i])

        return res
            