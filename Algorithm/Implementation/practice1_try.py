# 실전문제1 - 왕실의 나이트
# 입력된 위치에서 나이트가 이동할 수 있는 경우의 수 찾기
# 입력값은 'a1', 'c4' 이런 식으로 들어온다.
# 체스판 : 8 x 8
# 행 : 1~8
# 열 : a~h(ord('a') ~ ord('a')+7)

# 위, 아래, 좌, 우 각각 2방향으로 움직일 수 있음
import time

loc = input()

start = time.time()

col = ord(loc[0])-96 #계산 편의를 위해 a를 1로 변환한다
row = int(loc[1])

# 한 칸 움직이기 가능 여부 
def moveUpOnce():
    return row-1 >= 1 
def moveDownOnce():
    return row+1 <= 8 
def moveRightOnce():
    return col+1 <= 8 
def moveLeftOnce():
    return col-1 >=1 

# 두 칸 움직이기 가능 여부
def moveUpTwice():
    return row-2 >= 1 
def moveDownTwice():
    return row+2 <= 8 
def moveRightTwice():
    return col+2 <= 8 
def moveLeftTwice():
    return col-2 >=1 

# 나이트 움직이기 가능 여부
def canMoveRight():
    p = 0
    if moveRightTwice():
        if moveUpOnce():
            p+=1
        if moveDownOnce():
            p+=1
    return p
def canMoveLeft():
    p = 0
    if moveLeftTwice():
        if moveUpOnce():
            p+=1
        if moveDownOnce():
            p+=1
    return p
def canMoveUp():
    p = 0
    if moveUpTwice():
        if moveRightOnce():
            p+=1
        if moveLeftOnce():
            p+=1
    return p
def canMoveDown():
    p = 0
    if moveDownTwice():
        if moveRightOnce():
            p+=1
        if moveLeftOnce():
            p+=1
    return p

print(canMoveDown()+canMoveUp()+canMoveRight()+canMoveLeft())


print("time :",time.time()-start)