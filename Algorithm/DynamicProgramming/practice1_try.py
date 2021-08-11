# 실전문제 1 - 1로 만들기
# 연산 횟수 최소값 구하기

# 첫 번째 시도
# 최소값 구할 수 없음
x = int(input())
count = 0

def operation(x):
    global count
    count+=1
    if x == 1:
        return count
    if x%5==0:
        return operation(x//5)
    if x%3==0:
        return operation(x//3)
    if x%2==0:
        return operation(x//2)
    return operation(x-1)

print(operation(x))



