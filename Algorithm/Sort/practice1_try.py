# 실전문제 1 - 위에서 아래로

n = int(input())
li = [[0]*i for i in range(n)]
arr = []

for i in range(n):
    li[i] = int(input())
    arr.append(li[i])

li.sort(reverse=True)
arr = sorted(arr,reverse=True)

for i in li:
    print(i,end=' ')

for i in arr:
    print(i,end=' ')