# 설탕과자 뽑기
h,w = map(int,input().split()) # 세로, 가로 판 길이
ground = [[0]*w for _ in range(h)]

n = int(input()) # 막대 갯수
for i in range(n):
    l,d,x,y = map(int,input().split()) # 막대 정보 : 길이, 방향, 좌표(x,y) | d : 0은 가로, 1은 세로임
    ground[x-1][y-1] = 1 # 막대의 시작지점은 무조건 1

    #시작지점을 제외한 길이 계산
    if d == 0: #가로방향인 경우
        temp_y = y #막대 가로로 놓을 좌표 저장
        for j in range(l-1):
            ground[x-1][temp_y] = 1
            temp_y+=1
    else:
        temp_x = x #막대 세로로 놓을 좌표 저장
        for j in range(l-1):
            ground[temp_x][y-1] = 1
            temp_x+=1

for el in ground:
    for i in el:
        print(i,end=' ')
    print('')