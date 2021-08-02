# 예제 4-1 상하좌우
# R : 열 + 1
# L : 열 - 1
# U : 행 - 1
# D : 행 + 1

n = int(input()) # 공간의 크기
plan = list(input().split()) # 이동 계획서
loc = [1,1] # 여행자의 좌표. loc[0] : 행, loc[1] : 열

for i in plan:
    if i == 'R':
        if loc[1] != n:
            loc[1]+=1
    elif i == 'L':
        if loc[1] != 1:
            loc[1]-=1
    elif i == 'U':
        if loc[0] != 1:
            loc[0]-=1
    else:
        if loc[0] != n:
            loc[0]+=1

print('공간 :',n)
print('계획 :',plan)
print('좌표 : ',end=' ')
for i in loc:
    print(i,end=' ')