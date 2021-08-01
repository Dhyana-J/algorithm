# 바둑판 뒤집기
baduk = []
for i in range (19):
    baduk.append(list(map(int,input().split())))

n = int(input())

def change(row,col):
    for n in range(19):
        if n!=col:
            if baduk[row][n]==1:
                baduk[row][n]=0
            else:
                baduk[row][n]=1
        if n!=row:
            if baduk[n][col]==1:
                baduk[n][col]=0
            else:
                baduk[n][col]=1


for i in range(n):
    x,y = map(int,input().split())
    change(x-1,y-1)

for el in baduk:
    for i in el:
        print(i,end=' ')
    print('')
