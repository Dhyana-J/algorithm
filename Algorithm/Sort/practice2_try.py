# 실전문제 2 - 성적 낮은 순서대로 학생 출력하기

n = int(input())

li = []

for i in range(n):
    name,score = input().split()
    li.append((name,int(score)))

result = sorted(li,key=lambda x:x[1])

for i in result:
    print(i[0],end=' ')
