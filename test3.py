class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l, r = 0, 1
        buy_day = 0
        while l < len(prices):
            buy_day = prices[l]
            if prices[r] < prices[l]:
                buy_day = prices[r]
                l=r
                if r == len(prices)-1:
                    print(r, l)
                    r = l
                    print(r, l)
                else:
                    r+=1
        return buy_day
sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))

































# class Solution:
#     def findDuplicates(self, nums: list[int]) -> list[int]:
#         if len(nums) == 1:
#             return []
#         res = []
#         for n in nums:
#             i = abs(n)-1
#             print(f"i:{i}\nn:{n}\nnums[i]:{nums[i]}")
#             if nums[i] < 0:
#                 res.append(n)
#                 print(f"res:{res}\n\n")
#             else:
#                 print(f"-{nums[i]}\n\n")
#                 nums[i] = -1 * abs(nums[i])
#         return res



# print(sol.findDuplicates([10,1], [10,2,5,10,9,1,1,4,3,7]))





















# n = [1,7,3,6,5,6]
# print(sum(n[3+1:]))













# nums = [1,2,3,4]
# length = len(nums)

# runsum = [nums[0]].extend([0]*(length-1))
# print([0].extend([1]*3))
# print(f"{[nums[0]]}.extend([0]*({length}-1))")
# print(runsum)


















# class Solution:
#     def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
#         h = {}
#         # i = 0
#         #for i in range(len(nums))
#         for i, n in enumerate(nums):
#             print(h)
#             if n in h:
#               if abs(i-h[n]) <= k:
#                     print(f"True car {n} est dans la hashtable et abs({i}-{h[n]}) <= k, hashtable: {h}\ni: {i}, h[n]: {h[n]}, n: {n} ")
#                     return True
#               else:
#                   h[n] = i
#             else:
#               h[n] = i
#             # i+=1
#         return False
  
# sol = Solution()
# sol.containsNearbyDuplicate([1,4,2,3,1,2], 3)


















# l, r = 0, len(s) -1

#         while l < r:
#             while l < r and not self.isAlp(s[l]):
#                 l+=1
#             while r > l and not self.isAlp(s[r]):
#                 r-=1
#             if s[l].lower() != s[r].lower():
#                 return False
#             l, r = l+1, r-1
#         return True
#     def isAlp(self, c):
#         return (ord("A") <= ord(c) <= ord("Z") or
#                 ord("a") <= ord(c) <= ord("z") or
#                 ord("0") <= ord(c) <= ord("9"))






















# cons=0
# nums = [1,0,1,1,0,1]
# for i in range(len(nums)):
#     if i == len(nums)-1:
#         print(cons)
#         break

#     if (nums[i] == 1 and nums[i] == nums[i+1]):
#         cons+=1
        
# print(cons)
# print(f"answer: 2")















# target = 9
# nums = [2,7,11,15]
# dic = {n: target-n for n in nums}
# dic2 = {n:i for i, n in enumerate(nums)}
# print(dic2)

# dic = {n: target-n for n in nums}
# for num, soustr in dic.items():
#     if soustr in dic:
#         print(dic2[num], dic2[soustr])
#         break














# class QueueWithTwoStacks:
#   def __init__(self):
#     self.stack1 = []  # Pour enqueue
#     self.stack2 = []  # Pour dequeue
    
#   def enqueue(self, x):
#     self.stack1.append(x)
#   def dequeue(self):
#     # TODO : retire et retourne le premier élément
#     # Indice : utilise stack2, inverse stack1 si besoin
#     if self.stack2==[]:
#       self.stack2=self.stack1[::-1]
#       self.stack1=[]
#     pop = self.stack2.pop()
    
#     return pop

# # Test
# q = QueueWithTwoStacks()
# q.enqueue('A')
# q.enqueue('B')
# q.enqueue('C')
# print(q.dequeue())  # Doit afficher 'A'
# print(q.dequeue())  # Doit afficher 'B'
# q.enqueue('D')
# print(q.dequeue())  # Doit afficher 'C'
# print(q.dequeue())  # Doit afficher 'D'