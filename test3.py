
























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