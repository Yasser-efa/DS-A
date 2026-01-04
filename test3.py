class QueueWithTwoStacks:
  def __init__(self):
    self.stack1 = []  # Pour enqueue
    self.stack2 = []  # Pour dequeue
    
  def enqueue(self, x):
    self.stack1.append(x)
  def dequeue(self):
    # TODO : retire et retourne le premier élément
    # Indice : utilise stack2, inverse stack1 si besoin
    if self.stack2==[]:
      self.stack2=self.stack1[::-1]
      self.stack1=[]
    pop = self.stack2.pop()
    
    return pop

# Test
q = QueueWithTwoStacks()
q.enqueue('A')
q.enqueue('B')
q.enqueue('C')
print(q.dequeue())  # Doit afficher 'A'
print(q.dequeue())  # Doit afficher 'B'
q.enqueue('D')
print(q.dequeue())  # Doit afficher 'C'
print(q.dequeue())  # Doit afficher 'D'