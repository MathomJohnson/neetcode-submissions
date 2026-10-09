class Solution:
    def trap(self, height: List[int]) -> int:
        
        leftMax = [0] * len(height)
        best = 0
        for i in range(len(height)):
            leftMax[i] = best
            best = max(best, height[i])

        rightMax = [0] * len(height)
        best = 0
        for i in range(len(height) - 1, -1, -1):
            rightMax[i] = best
            best = max(best, height[i])

        res = 0

        for i in range(len(height)):
            if i == 0 or i == len(height) - 1:
                continue

            water = max(0, min(leftMax[i], rightMax[i]) - height[i])
            res += water

        return res
