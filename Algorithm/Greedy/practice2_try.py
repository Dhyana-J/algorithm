# 실전문제 2 - 숫자 카드 게임
import time

n,m = map(int,input().split())

# ground = []
max = 1

for _ in range(n):
    temp = min(list(map(int,input().split())))
    if temp > max:
        max = temp
print(max)

start = time.time()
# for _ in range(n):
    # temp = list(map(int,input().split()))
    # temp.sort()
    # ground.append(min(list(map(int,input().split()))))

# for li in ground:
#     for i in range(1):
#         if max < li[i]:
#             max = li[i]

# for i in ground:
#     if i > max:
#         max = i
    


print(time.time()-start)
