# 6098 - 성실한 개미

# 개미는 오른쪽 또는 아래로만 이동한다 (행이나 열이 +만 가능함)

# 판 만들기
ground = []
for i in range(10):
    ground.append(list(map(int,input().split())))

x = 1
y = 1
ground[x][y] = 9
IS_END = False


for col in range(10):
    if IS_END: 
        break
    for row in range(10):
        if ground[x][y+1] == 1:
            break
        else:
            y+=1
            if ground[x][y] == 2:
                ground[x][y] = 9
                IS_END = True
                break
            else:
                ground[x][y] = 9

    if ground[x+1][y] == 1:
        break
    else:
        x+=1
        if ground[x][y] == 2:
                ground[x][y] = 9
                IS_END = True
                break
        else:
            ground[x][y] = 9


# 최종 판 출력
for el in ground:
    for i in el:
        print(i,end=' ')
    print()