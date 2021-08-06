# quick sort (빠른 정렬)

"""
기준 데이터(pivot)를 설정하고, 피벗기준 그 기준보다 큰 데이터와 작은 데이터를 탐색해 위치를 바꾸는 기법. 
탐색하다가 두 데이터까지의 인덱스 합이 총 데이터 인덱스보다 큰 경우(엇갈린 경우),
피벗값과 데이터(오름차순인 경우 작은데이터, 내림차순인 경우 큰데이터) 위치를 바꾼다. 이런 식으로 피벗을 확장시켜나가면서 정렬을 수행한다.

평균 시간 복잡도는 O(NlogN) 이다. 최악의 경우는 O(N^2)
일반적으로, 컴퓨터과학에서의 log는 밑이 2인 로그를 의미!
"""

arr = list(map(int,'5790316248'))

def quick_sort(arr,start,end):
    if start>=end: #원소가 한 개인 경우 종료
        return
    pivot = start #첫 번째 원소부터 피벗으로 지정
    left = start+1
    right = end

    while left<=right:
        # 피벗보다 큰 데이터 찾을 때 까지 반복
        while left<=end and arr[left]<=arr[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때 까지 반복
        while right>start and arr[right]>=arr[pivot]:
            right -= 1
        # 엇갈린 경우
        if left > right:
            arr[pivot],arr[right] = arr[right],arr[pivot]
        # 엇갈리지 않은 경우
        else:
            arr[left],arr[right] = arr[right],arr[left]

    # 분할 이후, 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행 
    # right는 이전 피벗이 있는 자리이므로, 양 옆의 배열에 대해 퀵 정렬을 수행한다.
    quick_sort(arr,start,right-1)
    quick_sort(arr,right+1,end)

quick_sort(arr,0,len(arr)-1)

print(arr)


