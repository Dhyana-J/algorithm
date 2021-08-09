# 실전문제 2 - 떡볶이 떡 만들기
# 적어도 M만큼의 떡을 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값 구하기
# 떡을 자르고 난 나머지를 손님이 가져가는것 
# sum(ttuck[i]%h) >= m 이어야함

# 순차탐색
# 한계 : 좁은 범위면 몰라도 이 문제 탐색 범위가 10억이다. 순차탐색 연산량 너무 많음 시간초과우려
n, m = map(int,input().split()) # 떡 개수, 길이 입력받기
ttuck = sorted(list(map(int,input().split()))) # 떡의 개별 높이
h = ttuck[len(ttuck)-1] # 가장 긴 길이부터 설정해서 만족하는 길이 찾아나가자
while True:
    l = m
    for i in ttuck:
        r = i-h
        if r<0:
            r = 0
        l -= r # 떡을 잘라 손님에게 주며 요청한 길이 차감
        if l<=0:
            break
    if l <= 0:
        print(h)
        break
    else:
        h-=1


