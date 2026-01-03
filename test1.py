from jovian.pythondsa import evaluate_test_case as ev
# [32, 21, 16, 15, 12, 8, 7, 4, 2]

def locate_card(cards, query):
  left = 0
  right = len(cards) - 1
  if cards == []:
    return -1
  while left <= right:
    mid = (left + right) // 2
    if cards[mid] == query:
      return mid
    elif query < cards[mid]:
     left = mid + 1
    else:
      right = mid - 1
  return -1

# query occurs in the middle
test = {
    'input': { 
        'cards': [13, 11, 10, 7, 4, 3, 1, 0], 
        'query': 7
    },
    'output': 3
}

test1={
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 1
    },
    'output': 6
}

# query is the first element
test2={
    'input': {
        'cards': [4, 2, 1, -1],
        'query': 4
    },
    'output': 0
}

# query is the last element
test3={
    'input': {
        'cards': [3, -1, -9, -127],
        'query': -127
    },
    'output': 3
}

# cards contains just one element, query
test4={
    'input': {
        'cards': [6],
        'query': 6
    },
    'output': 0 
}

# cards does not contain query 
test5={
    'input': {
        'cards': [9, 7, 5, 2, -9],
        'query': 4
    },
    'output': -1
}

# cards is empty
test6={
    'input': {
        'cards': [],
        'query': 7
    },
    'output': -1
}

# numbers can repeat in cards
test7={
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 3
    },
    'output': 7
}

# query occurs multiple times
test8={
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
    },
    'output': 2
}

ev(locate_card, test8)