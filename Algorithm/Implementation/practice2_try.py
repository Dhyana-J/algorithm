# 실전문제2 - 게임 개발
# 방위 -> 0,1,2,3 : 북,동,남,서
# 맵 육지or바다 표기 -> 0,1 : 육지,바다
# 방문한곳은 2로 표기하자

"""
@ 이동 방법

현재 방향 기준 왼쪽으로 갈 수 있는지 체크(육지면서 안가본 칸인 경우)
    갈 수 있다면 왼쪽으로 돌고 간다
    갈 수 없다면 왼쪽으로 돌기만 한다
초기 방향으로 돌아온 경우 방위 유지하며 뒤로 간다.(뒤가 바다이면 종료) 

"""
# 이동을 마친 후 캐릭터가 방문한 칸의 수 출력하기

import time

n,m = map(int,input().split()) # n x m 체스판 만들 때 쓸 변수
a,b,d = map(int,input().split()) # 캐릭터 좌표, 바라보는 방향
rotation = 0

moveLeft = [
        [0,-1], # 북쪽을 보고있는 경우 왼쪽으로 이동할 때 쓸 좌표
        [-1,0], # 동쪽 기준 왼쪽 이동
        [0,1], # 남쪽
        [1,0] # 서쪽
    ]
moveBack = [
    [1,0], # 북 기준 뒤로 이동
    [0,-1], # 동
    [-1,0], # 남
    [0,1] # 서
]

# 맵 생성
ground = []
for i in range(n):
    ground.append(list(map(int,input().split())))

start = time.time()

ground[a][b] = 2 # 시작지점 방문처리

def turnLeft():
    global d
    if d == 0:
        d = 3
    elif d == 1:
        d = 0
    elif d == 2:
        d = 1
    elif d == 3:
        d = 2

while True:
    if rotation == 4:
        r = a+moveBack[d][0] # 이동 예정 위치 행
        c = b+moveBack[d][1] # 이동 예정 위치 열
        if r >= 0 and r < n and c < m and c >= 0: #이동 위치 좌표가 맵 안쪽인 경우
            if ground[r][c] == 1:
                break
            else:
                ground[r][c] = 2
                a = r
                b = c
        else:
            break
    else:
        r = a+moveLeft[d][0]
        c = b+moveLeft[d][1]
        if r >= 0 and r < n and c < m and c >= 0:
            if ground[r][c] == 0 : # 왼쪽이 방문 안한 육지인 경우
                #왼쪽으로 회전 
                turnLeft()
                rotation+=1
                #이동
                ground[r][c] = 2
                a = r
                b = c
                

            else: # 왼쪽이 바다이거나 방문한 경우
                #왼쪽으로 회전 
                turnLeft()
                rotation+=1
        else: # 이동 위치 좌표가 맵 바깥인 경우
            #왼쪽으로 회전 
            turnLeft()
            rotation+=1
            


print('==============')

result = 0

# 결과 출력
for i in ground:
    for j in i:
        if j==2:
            result+=1
        print(j,end=' ')
    print()

print(result)

print('time : ',time.time()-start)