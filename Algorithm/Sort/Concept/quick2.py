arr = list(map(int,'5790316248'))


def quick_sort(arr):
    if len(arr)<=1:
        return arr
    
    pivot = arr[0] # 피벗
    tail = arr[1:] # 피벗 제외한 리스트

    left_side = [x for x in tail if x<pivot]
    right_side = [x for x in tail if x>=pivot]

    return quick_sort(left_side)+[pivot]+quick_sort(right_side)

print(quick_sort(arr))
    