
def find_averages_of_subarrays(arr, K):

    result = []

    for i in range(len(arr)- K +1):
        sum = 0.0
        for j in range(i, i+K):
            sum += arr[j]
            print("sum range(i, i+K)", sum)
        result.append(sum/K)
        print("sum/k", sum/K)
    return result


K = 5
arr = [2, 4, 6, 8, 2, 4, 6] # --> ([4.4, 4.8, 5.2])
print(find_averages_of_subarrays(arr, K))