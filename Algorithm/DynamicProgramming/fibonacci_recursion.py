import time
start = time.time()
"""재귀적으로 구현한 피보나치. 시간복잡도는 O(2^N)으로 어마어마함"""
# def fibo(x):
#     if x==1 or x==2:
#         return 1
#     return fibo(x-1)+fibo(x-2)


"""메모이제이션 활용한 피보나치. 시간복잡도는 O(N) f(n)을 구한 값이 f(n+1)에 활용됨"""
# 한번 계산된 결과를 메모이제이션 하기 위한 리스트 초기화
d = [0]*100

# 피보나치 함수를 재귀함수로 구현 (탑다운 다이나믹 프로그래밍)
def fibo(x):
    if x==1 or x==2:
        return 1
    if d[x]!=0: # 계산한 적 있는 문제라면 그대로 반환
        return d[x]
    # 아직 계산하지 않은 문제라면 점화식에 따라 피보나치 결과 반환
    d[x] = fibo(x-1)+fibo(x-2)
    return d[x]

print(fibo(99))
print('time : ',time.time()-start)