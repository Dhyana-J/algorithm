import heapq #모듈 이름이랑 파일 이름이랑 같으면 에러난다. 주의하자!

def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h,value)
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

print(heapsort([1,3,5,7,9,2,4,6,8,0]))

