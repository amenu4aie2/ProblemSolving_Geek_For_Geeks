# User function Template for python3

class Solution:
    def longestSubarray(self, arr, k):  
        prefix_sum = 0
        max_length = 0
        prefix_sum_map = {}
    
        for i, num in enumerate(arr):
            prefix_sum += num
    
            # Check if the current prefix_sum equals k
            if prefix_sum == k:
                max_length = i + 1
    
            # Check if (prefix_sum - k) exists in the map
            if (prefix_sum - k) in prefix_sum_map:
                max_length = max(max_length, i - prefix_sum_map[prefix_sum - k])
    
            # Add the current prefix_sum to the map if not already present
            if prefix_sum not in prefix_sum_map:
                prefix_sum_map[prefix_sum] = i
    
        return max_length
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        print(ob.longestSubarray(arr, k))
        tc -= 1
        print("~")
# } Driver Code Ends