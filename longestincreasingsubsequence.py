# Longest Increasing Subsequence
# Send Feedback
# Given an array with N elements, you need to find the length of the longest subsequence in the given array such that all elements of the subsequence are sorted in strictly increasing order.
# Input Format
# The first line of input contains an integer N. The following line contains N space separated integers, that denote the value of elements of array.
# Output Format
# The first and only line of output contains the length of longest subsequence.
# Constraints
# 1 <= N <= 10 ^ 3
# Time Limit: 1 second
# Sample Input 1:
# 6
# 5 4 11 1 16 8
# Sample Output 1:
# 3
# Sample Output Explanation
# Length of longest subsequence is 3 i.e. (5, 11, 16) or (4, 11, 16).
# Sample Input 2:
# 3
# 1 2 2
# Sample Output 2:
# 2
def lis(arr):
    #   Implement Your Code Here
    n = len(arr)
    lis = [1]*n
    for i in range(1, n):
        for j in range(0, i):

        """Recursively get all LIS ending with arr[0], arr[1]..arr[n-2]
       IF arr[n-1] is maller than arr[n-1], and max ending with
       arr[n-1] needs to be updated, then update it"""

        if arr[i] > arr[j] and lis[i] < lis[j] + 1:
            lis[i] = lis[j]+1

	# Compare maxEndingHere with overall maximum. And
    # update the overall maximum if needed
    maximum = 0
    for i in range(n):
        maximum = max(maximum, lis[i])

    return maximum


p = int(input())
li = [int(ele) for ele in input().split()]
print(lis(li))
