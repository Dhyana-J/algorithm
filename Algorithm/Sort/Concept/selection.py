# selection sort (선택 정렬) : 가장 작은 수를 찾아 앞으로 보내고, 그 다음 작은 수를 앞에서 두 번째로 보내고, ... 반복하는 정렬방법
# 시간복잡도가 O(N^2) 이므로, 데이터가 많아지면 급격하게 느려진다. 다른 정렬 알고리즘보다 비효율적


import time
start = time.time()

arr = [i for i in range(10000)]

def selection_sort():
    for i in range(len(arr)-1):
        min_idx = i
        for j in range(i+1,len(arr)):
            if arr[min_idx]>arr[j]: 
                min_idx = j
        arr[i],arr[min_idx] = arr[min_idx],arr[i] # 파이썬에서 제공하는 스왑기능

selection_sort()
print(arr)
print('end time : ',time.time()-start)
