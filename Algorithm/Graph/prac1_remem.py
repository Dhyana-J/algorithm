
n,m = map(int,input().split())

ground = []

for i in range(n):
    ground.append(list(map(int,input()))) # map을 통해 문자열 한글자씩 리스트 요소로 쓴다

print(ground)
def dfs(x,y):
    if x>=n or x<0 or y>=m or y<0:
        return False

    if ground[x][y]==0:
        ground[x][y] = 1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result+=1

print(result)