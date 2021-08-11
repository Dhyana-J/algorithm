# 실전문제 4 - 효율적인 화폐 구성

n,m = map(int,input().split())
array = []

for i in range(n):
    array.append(int(input()))

d = [10001] * (m+1) # index m까지 DP table 생성

d[0] = 0
for i in range(n):
    for j in range(array[i],m+1):
        d[j] = min(d[j],d[j-array[i]]+1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
