# insertion sort (삽입 정렬) : 특정한 데이터를 적절한 위치에 삽입하는 정렬 방법. 탐색 인덱스 앞부분은 오름차순정렬되어있다고 가정
# 시간복잡도 O(N^2)로 선택 정렬과 같지만, 거의 정렬된 리스트에 사용하면 매우 빠르다! 최선의 시간복잡도는 O(N)이다.

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1,len(arr)):
    for j in range(i,0,-1):
        if arr[j]<arr[j-1]:
            arr[j],arr[j-1] = arr[j-1],arr[j]
        else:
            break

print(arr)