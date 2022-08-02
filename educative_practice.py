####################################################################################
# 07.31.2022 Sliding Windows
####################################################################################
"""
Given an array, find the average of all subarrays of ‘K’ contiguous elements in it.
"""

#Option Brute-force. 
"""
Time complexity O (N * K) Since for every element of the input array, 
we are calculating the sum of its next ‘K’ elements, the time complexity of the above 
algorithm will be O(N*K) where ‘N’ is the number of elements in the input array.
"""
def find_averages_of_subarrays_brute(arr, K):

    result = []
    sum = 0.0
    for i in range(len(arr)- K +1):
        
        for j in range(i, i+K):
            sum += arr[j]
        result.append(sum/K)
    return result
'''
index: 0 1 2 3 4 5 6
subarr: 0 1 2 3 4
        1 2 3 4 5
        2 3 4 5 6
arr:   2 4 6 8 2 4 6
result : [((2 + 4 + 6 + 8 + 2)/5) , ((4 + 6 + 8 + 2 + 4)/5 ) , (6 + 8 + 2 + 4 + 6)/5 ]
i=0 i=1 i=2
j:  j=0 j=1 j=2 j=3 j=4
    j=1 j=2 j=3 j=4 j=5
    j=2 j=3 j=4 j=5 j=6
sum=  6 + 8 + 2 + 4 + 6
avr= (6 + 8 + 2 + 4 + 6)/5 
range(len(arr)- K -1): 0 to (7 - 5 +1)= 3 (aka 2)
range(i, i+K): 0 to 5( aka 4) 
               1 to 6( aka 5) 
               2 to 7( aka 6)

main...
K = 5
arr = [2, 4, 6, 8, 2, 4, 6]
print(find_averages_of_subarrays_brute(arr, K))

'''

#Option Sliding Window 

"""
This will save us from going through the whole subarray to find the sum and, as a result, the algorithm complexity will reduce to O(N)
O(N).
"""

def find_averages_of_subarrays(arr, K):
    result = []
    windowSum = 0.0
    for i in range(len(arr)):
        windowSum += arr[i]
        if i >= K - 1:
            result.append(windowSum/K)
            windowSum -= arr[i - K + 1]
    return result

"""
K = 5
arr = [2, 4, 6, 8, 2, 4, 6]
print(find_averages_of_subarrays(arr, K))
"""