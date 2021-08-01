# 입체기동장치 생산공장

n = int(input())

machineList = []

for i in range(n):
    a,b = map(int,input().split())
    machineList.append((a,b))

result = sorted(machineList, key=lambda x:x[0])

for el in result:
    for i in el:
        print(i,end=' ')
    print()
    