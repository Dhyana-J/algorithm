# parametric search 유형의 문제이다.
# 보통 이런 유형은 이진 탐색을 통해 해결한다.
# 일반적으로 파라메트릭 서치 유형은 재귀가 아닌 반복문 형태로 구현하면 더 간결하다.

""" 
Q. 이진 탐색으로 이 문제를 어떻게 해결할까?

이진탐색은 최소값, 중간값, 최대값을 설정해 탐색해나간다.

여기서 탐색할 값은 절단기에 설정할 높이 (h)다.

h의 최소값은 0, 최대값은 가장 긴 떡의 높이 값이다.

떡 개수 : 4
손님이 원하는 떡 길이 : 6
보유한 떡 : [19, 15, 10, 17]

# 과정
왼쪽에서부터 최소 중간 최대 절단기 설정 길이 h
t1 : 0 9 19  #h=9, 자르고 얻은 떡길이는 10+6+1+8 = 25다. 얻을 수 있는 떡 길이가 손님이 원하는 값 6보다 훨씬 크므로, 시작점을 mid+1로 증가시킨다.
t2 : 10 14 19 #h=14, 5+1+0+3 = 9. 얻을 수 있는 떡 길이가 손님이 원하는 값보다 크다. 시작점 mid+1
t3 : 15 17 19 #h=17, 2+0+0+0 = 2. 손님이 원하는 값보다 작음. 끝점 mid-1
t4 : 15 15 16 #h=15, 4+0+0+2 = 6. 손님이 원하는 값에 딱 맞다. 최적의 길이는 h=15임을 알 수 있다.
"""

n, m = map(int,input().split()) # 떡 개수, 길이 입력받기
ttuck = sorted(list(map(int,input().split()))) # 떡의 개별 높이
start = 0
end = max(ttuck)

result = 0

while(start<=end):
    total = 0
    mid = (start+end)//2
    for x in ttuck:
        if x > mid:
            total += x-mid
    if total<m:
        end = mid-1
    else:
        result = mid
        start = mid+1


#재귀로 해보기
# def binary_search(target,start,end):
#     global result
#     if start>end:
#         return None
#     mid = (start+end)//2
#     total = 0;
#     for i in ttuck:
#         if i-mid > 0:
#             total+=i-mid
#     if total < target:
#         return binary_search(target,start,mid-1)
#     else:
#         result = mid
#         return binary_search(target,mid+1,end)
# binary_search(m,0,end);

print(result)