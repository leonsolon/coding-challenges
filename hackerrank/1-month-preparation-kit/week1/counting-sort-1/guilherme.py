def countingSort(arr):
    count = [0]*100
    for a in arr:
        count[a] +=1

    return count

assert countingSort([1,1,3,2,1]) == [0,3,1,1] + [0]*(100-4)
assert countingSort([0]*20 + [1]*30 + [2]*8+[99]*10) == [20,30,8] + [0]*(100-4) + [10]