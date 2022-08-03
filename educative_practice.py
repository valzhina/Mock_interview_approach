####################################################################################
# Sliding Windows
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
    for i in range(len(arr)- K +1):
        sum = 0.0
        
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

####################################################################################
# Smallest Subarray With a Greater Sum
####################################################################################
"""
Given an array of positive integers and a number ‘S,’ find the length of 
the smallest contiguous subarray whose sum is greater than or equal to ‘S’. 
Return 0 if no such subarray exists.
"""
def smallest_subarray_sum(s, arr):

    windowSum = 0.0
    min_length = len(arr)
    window_start = 0

    for i in range(len(arr)):
        windowSum += arr[i]
        while windowSum >= s:
            # remember the length of this window as the smallest window so far
            min_length = min(min_length, i - window_start + 1) 
            windowSum -= arr[window_start]
            window_start += 1
    if min_length == len(arr):
        return 0
    return min_length

"""

    i=0 (range 0 to 6)
    i=1    windowSum = 2 < 7
    i=2    windowSum = 2+1+5 =8 / < 7
    i=3    windowSum = 1+5+2 =8 / < 7
    i=4    windowSum = 5+2+3 =10 / < 7
    i=5    windowSum = 2+3+2 =7 / <= 7

        while yes
            min_length = min(3, 5 - 3 + 1 ) = 3
            windowSum = 7-2->5
            window_start =  0->1->2->3->4
    return 3

The time complexity of the above algorithm will be O(N)
The outer for loop runs for all elements, and the inner while loop processes 
each element only once; therefore, the time complexity of the algorithm will be O(N+N),
which is asymptotically equivalent to O(N)
"""

'''
# s = 7
# arr = [2, 1, 5, 2, 3, 2] # --> 2
# s = 8
# arr = [3, 4, 1, 1, 6] # --> 3
# s = 8
# arr = [2, 1, 5, 2, 3, 2] # --> 3
# s = 8
# arr = [0] # --> 3

print(smallest_subarray_sum(s, arr))
'''

####################################################################################
# Longest Substring with maximum K Distinct Characters
####################################################################################
"""
Given a string, find the length of the longest substring in it with no more than 
K distinct characters.
"""