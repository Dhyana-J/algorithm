# 이진탐색, 계수정렬, set함수 사용해서 풀 수 있다.

""" 계수정렬 """
# n = int(input())
# store = [0]*100000

# # 가게 전체 부품번호 기록
# for i in input().split():
#     store[int(i)] = 1

# m = int(input())
# order = list(map(int,input().split()))

# for i in order:
#     if store[i] == 1:
#         print('yes',end=' ')
#     else:
#         print('no',end=' ')

""" set() 이용 """
n = int(input())
store = set(map(int,input().split()))
print(store)

m = int(input())
order = list(map(int,input().split()))

for i in order:
    if i in store:
        print('yes',end=' ')
    else:
        print('no',end=' ')