class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        absolute = [abs(x) for x in nums]
        if min(absolute) in nums:
            return min(absolute)
        return -min(absolute)

    # Time: O(2n) -> O(n)
    # Space: O(1)

sol = Solution
test = [24, 14, 90, -2, 2, -1]
print(sol.findClosestNumber(sol, nums=test))