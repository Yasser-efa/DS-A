class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        if len(nums) == k:
            return sum(nums) / k
        

sol = Solution()
print(sol.findMaxAverage([1,12,-5,-6,50,3,4,2,-2,5,-6,-200,5,100000], 4))


# class Solution:
#     def rotate(self, nums: list[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         if k == 0:
#             return nums
#         k = k%len(nums)
#         self.l, self.r = 0, len(nums)-1
#         nums = self.reverse(nums)


#         self.l, self.r = 0, k-1
#         nums = self.reverse(nums)

#         self.l, self.r = k, len(nums)-1
#         return nums
    
#     def reverse(self, n):
#         t = 0
#         while self.l < self.r:
#             t = n[self.l]
#             n[self.l] = n[self.r]
#             n[self.r] = t
#             self.l+=1
#             self.r-=1
#         return n


# nums = [1,2,3]
# sol = Solution()
# print(sol.rotate(nums, 5))