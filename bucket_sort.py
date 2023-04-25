def bucket_sort(arr):
    # Find the maximum value in the array and calculate the bucket size
    max_val = max(arr)

    # Create empty buckets
    buckets = [[] for _ in range(len(arr))]

    # Assign each element to a bucket based on its value
    for val in arr:
        index = int(val / len(arr))
        buckets[index].append(val)

    # Sort each bucket and concatenate them into a sorted list
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))

    return sorted_arr


arr = [5, 3, 8, 6, 4]
sorted_arr = bucket_sort(arr)
print(sorted_arr)  # Output: [3, 4, 5, 6, 8]