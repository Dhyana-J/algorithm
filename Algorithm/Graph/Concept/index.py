# DFS(Depth First Search) / BFS(Breadth First Search) : 그래프를 탐색하기 위한 대표적인 두 가지 알고리즘

""" Stack & Queue """
# from collections import deque

# stack = []
# stack.append(0)
# stack.append(2)
# stack.pop()
# stack.append(1)
# stack.append(3)

# print('stack :',stack[2:0:-1])


# queue = deque()

# queue.append(1)
# queue.append(2)
# queue.append(3)
# queue.popleft()

# print('queue :',list(queue))

""" Recursive Function """
import time
start = time.time()
def factorial_recursion(n):
    if n==1:
        return 1
    else:
        return n*factorial_recursion(n-1)

def factorial_iteration(n):
    result = 1
    for i in range(n,1,-1): # n부터 1+1 까지 감소하면서 반복
        print(i)
        result = result*i
    return result
    
# print(factorial_recursion(5))
print(factorial_iteration(5))
print('time :',(time.time()-start))
