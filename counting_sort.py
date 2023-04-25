def counting_sort(arr):
    max_val = max(arr)
    amount = [0]*(max_val+1)

    for num in arr:
        amount[num] += 1

    res = []
    for i in range(len(amount)):
        res.extend([i] * amount[i])
    return res


print(counting_sort([1,6,2,5,3,4]))

