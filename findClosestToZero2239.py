class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        closest = nums[0]
        for x in nums:
            if abs(closest) > abs(x):
                closest = x
        if closest < 0 and closest in nums:
            return abs(closest)
        else:
            return closest

    # Time: O(2n) -> O(n)
    # Space: O(1)

sol = Solution
test = [24, 14, 90, -2, 2, -1]
print(sol.findClosestNumber(sol, nums=test))