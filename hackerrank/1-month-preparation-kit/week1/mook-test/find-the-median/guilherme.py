def findMedian(arr):
    arr.sort()
    len_arr = len(arr)
    median = arr[len_arr//2]
    return median