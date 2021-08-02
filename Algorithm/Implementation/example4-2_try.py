# 예제 4-2 시각
# 00~n시 00~59분 00~59초
import time
n = int(input())
count = 0
start = time.time()

for h in range(n+1): #시
    for m in range(59+1): #분
        for s in range(59+1): #초
            if s%10==3 or m%10==3 or h%10 == 3 or s//10 == 3 or m//10 == 3:
                count+=1

print(count)
print('time : %.2f'%(time.time()-start))

