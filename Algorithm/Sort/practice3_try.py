# 실전문제 3 - 두 배열의 원소 교체

n,k = map(int,input().split())

a = sorted(list(map(int,input().split())))
b = sorted(list(map(int,input().split())),reverse=True)

result = 0

for i in range(n):
    if i < k and a[i] < b[i]:
        result+=b[i]
    else:
        result+=a[i]

print(result)

