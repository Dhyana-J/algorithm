# 실전문제 1 - 큰 수의 법칙

# 배열 크기 n, 총 덧셈 횟수 m, 한 인덱스당 연속덧셈 한계 k
# m >= k 조건이 만족되어야한다.

import time


n,m,k = map(int,input().split()) 

while m < k:
    print('m은 k보다 같거나 커야 합니다')
    n,m,k = map(int,input().split())

arr = list(map(int,input().split()))
start = time.time()
arr.sort(reverse=True)

# arr = sorted(list(map(int,input().split())),reverse=True)


count = 0
backFlag = False
result = 0

index = 0
while index < len(arr):
    for i in range(k):
        result+=arr[index]
        count+=1
        print(arr[index],count)
        if count==m:
            break
        else:
            if backFlag==True:
                break
    if count==m:
        break
    else:
        if backFlag==True:
            index-=1
            backFlag=False
            continue

    # 현재 값이 다음 값보다 크면 백플래그 활성화
    if arr[index] > arr[index+1]:
        backFlag = True
    index+=1

    
print(result)

print('processing time : ','%.2f'%(time.time()-start))

