x = int(input())

# 계산 결과 저장을 위한 DP테이블 초기화
# d[x] = 연산 횟수
d = [0]*30001

# 각 연산 결과를 차례대로 비교해서, 연산 횟수가 가장 적은 것을 대입한다.
for i in range(2,x+1):
    # 현재 수에서 1 빼는 경우
    d[i] = d[i-1] + 1
    if i%2==0:
        d[i] == min(d[i],d[i//2]+1)
    if i%3==0:
        d[i] = min(d[i],d[i//3]+1)
    if i%5==0:
        d[i] = min(d[i],d[i//5]+1)

print(d[x])

for i in range(x+1):
    print(d[i],end=' ')
