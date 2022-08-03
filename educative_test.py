
def smallest_subarray_sum(s, arr):

    windowSum = 0.0
    min_length = len(arr)
    window_start = 0

    for i in range(len(arr)):
        windowSum += arr[i]
        while windowSum >= s:
            min_length = min(min_length, i - window_start + 1)
            windowSum -= arr[window_start]
            window_start += 1
    if min_length == len(arr):
        return 0
    return min_length



# s = 7
# arr = [2, 1, 5, 2, 3, 2] # --> 2
# s = 8
# arr = [3, 4, 1, 1, 6] # --> 3
# s = 8
# arr = [2, 1, 5, 2, 3, 2] # --> 3
# s = 8
# arr = [0] # --> 3

print(smallest_subarray_sum(s, arr))