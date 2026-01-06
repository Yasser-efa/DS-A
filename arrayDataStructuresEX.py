from collections import deque
expenses = {
  "January": 2200,
  "February": 2350,
  "March": 2600,
  "April": 2130,
  "May": 2190
}

# 1. In Feb, how many dollars you spent extra compare to January?
print(expenses['February'])

# 2. Find out your total expense in first quarter (first three months) of the year.
totalExpenses = 0
for month, exp in expenses.items():
  totalExpenses += exp
print(totalExpenses)

# 3. Find out if you spent exactly 2000 dollars in any month
if 2000 in expenses.values():
  print("Yes")
else:
  print('No')
  
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
expenses["June"] = 1980
print(expenses)

# 5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this

expenses["April"] -= 200
print(expenses)

# EX2:

heros=['spider man','thor','hulk','iron man','captain america']
print(len(heros))

heros.append("black panther")
bp = heros.pop()
heros.insert(3, bp)
heros[1:3]=["doctor strange"]
heros.sort()
print(heros)

# EX3 Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function

def oddNum(max):
  odd_numbers = []

  for i in range(1, max):
    if i % 2 == 1:
        odd_numbers.append(i)

  print("Odd numbers: ", odd_numbers) 

print(oddNum(100))


m = "march 6"
march = [ord(i) for i in m]
print(sum(march)%100)