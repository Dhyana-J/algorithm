# Sequential Search (순차 탐색) - 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례로 확인하는 방법
# 최악의 시간복잡도는 O(N)

def sequential_search(n,target,array):
    for i in range(n):
        if array[i]==target:
            return i+1

print('생성할 원소 개수 입력 후 띄어쓰기 후 찾을 문자열 입력')

input_data = input().split()
n = int(input_data[0])
target = input_data[1]

print('원소 개수만큼 문자열 입력, 구분은 띄어쓰기 한 칸으로')
array = input().split()

print(sequential_search(n,target,array))