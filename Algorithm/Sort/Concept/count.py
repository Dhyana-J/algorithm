# Count Sort (계수 정렬)
"""
데이터의 모든 범위를 담을 수 있는 크기의 리스트(배열)이 필요한 알고리즘이다.
데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때만 사용 가능하다.
일반적으로 가장 큰 데이터와 가장 작은 데이터의 차이가 백만을 넘지 않을 때 효과적으로 사용

선택,삽입,퀵 정렬처럼 비교기반 알고리즘이 아니다.

데이터의 범위를 인덱스로 가지는 배열을 선언한 뒤, 각 데이터가 몇 번 씩 등장했는지 인덱스마다 기록하고, 
출력해주면 된다.

모든 데이터가 양수인 상황에서 데이터의 개수를 N, 데이터의 최대값을 K라고 할 때,
계수정렬의 시간 복잡도는 O(N+K)이다. 
현존하는 정렬 알고리즘 중 기수 정렬과 더불어 가장 빠르다.
"""

# 모든 원소의 값이 0보다 크거나 같다고 가정한다.

arr = list(map(int,'759031629148052'))

count = [0]*(max(arr)+1)

for i in range(len(arr)):
    count[arr[i]]+=1

for i in range(len(count)):
    for j in range(count[i]):
        print(i,end=' ')

