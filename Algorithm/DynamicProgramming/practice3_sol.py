# 실전문제 3 - 바닥 공사
# 점화식 : a(i) = a(i-1) + a(i-2)*2
# i는 바닥 가로길이
# a는 타일 채우는 경우의 수

n = int(input())

d = [0] * 1001
d[1] = 1
d[2] = 3
for i in range(3,n+1):
    d[i] = d[i-1]+d[i-2]*2%796796

print(d[n])
