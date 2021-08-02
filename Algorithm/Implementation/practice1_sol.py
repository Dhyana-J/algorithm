import time

input_data = input()
start = time.time()
row = int(input_data[1])
col = int(ord(input_data[0]))-int(ord('a'))+1

steps = [
    (-2,-1),(-2,1), # 아래
    (2,-1),(2,1), # 위
    (1,2),(-1,2), # 우
    (1,-2),(-1,-2) # 좌
]

result = 0
for step in steps:
    next_row = row+step[0]
    next_col = col+step[1]
    if next_row >= 1 and next_row <= 8 and next_col <= 8 and next_col >=1:
        result+=1

print(result)
print(time.time()-start)