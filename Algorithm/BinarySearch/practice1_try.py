# 실전 문제 1 - 부품 찾기
import time

n = int(input())
store = sorted(list(map(int,input().split())))

m = int(input())
order = sorted(list(map(int,input().split())))

start = time.time()

# 순차탐색
# for i in order:
#     find = False
#     for j in store:
#         if j==i:
#             find=True
#     if find:
#         print('yes',end=' ')
#     else:
#         print('no',end=' ')


# 이진탐색
# 최악의 경우 시간복잡도 O((M+N)logN) (정렬하고 이진탐색하는것 까지)
def bi_search(array,target,start,end):
    if start>end:
        return None
    mid = (start+end)//2
    if array[mid] == target:
        return True
    elif array[mid] > target:
        return bi_search(array,target,start,mid-1)
    elif array[mid] < target:
        return bi_search(array,target,mid+1,end)
    return None


for i in order:
    # 손님이 요청한 물건이 있으면 yes 없으면 no
    if bi_search(store,i,0,len(store)-1):
        print('yes', end=' ')
    else:
        print('no',end=' ')




print()
print('time : ',time.time()-start)