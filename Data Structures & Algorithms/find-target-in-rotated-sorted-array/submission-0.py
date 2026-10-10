class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        offset = l

        l, r = 0 + offset, len(nums) - 1 + offset

        while l <= r:
            mid = ((l + r) // 2)

            if nums[mid%len(nums)] == target: return mid%len(nums)
            elif nums[mid%len(nums)] < target: l = mid + 1
            else: r = mid - 1

        return -1