
def find_averages_of_subarrays(arr, K):
    result = []
    windowSum = 0.0
    for i in range(len(arr)):
        windowSum += arr[i]
        if i >= K - 1:
            result.append(windowSum/K)
            windowSum -= arr[i - K + 1]
    return result

K = 5
arr = [2, 4, 6, 8, 2, 4, 6]
print(find_averages_of_subarrays(arr, K))