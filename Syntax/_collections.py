from collections import deque, Counter

data = deque([2,3,4])

data.appendleft(5)
data.append(7)
print(data)

print('=================')

counter = Counter(['red','blue','red','green','green','black','green'])

print(counter)