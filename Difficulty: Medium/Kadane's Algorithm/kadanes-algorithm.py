#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    

    def maxSubArraySum(self,arr):
        cursum=float('-inf')
        umaxsum=float('-inf')
        for i in range(len(arr)):
            cursum=max(cursum+arr[i],arr[i])
            umaxsum=max(umaxsum,cursum)

        
        return umaxsum

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.maxSubArraySum(arr))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends