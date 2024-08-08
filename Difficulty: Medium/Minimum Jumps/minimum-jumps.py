class Solution:
    def minJumps(self, arr, n):
        if n == 1:
            return 0  # If there's only one element, no jumps are needed.

        jumps = 1  # We need at least one jump initially
        mr = arr[0]  # Maximum reachable index
        temp = arr[0]  # Temporary variable to store the max reach in the current window
        index = 1  # Start from the first index since arr[0] is the initial jump

        if mr == 0:
            return -1  # If the first element is 0, we can't move anywhere.

        for i in range(1, n):
            if i == n - 1:
                return jumps  # If we've reached the end of the array

            temp = max(temp, i + arr[i])

            if i == mr:  # When we reach the end of the current jump's reach
                jumps += 1
                mr = temp  # Update mr to the furthest we can reach
                if mr >= n - 1:  # If the maximum reach is beyond the last index
                    return jumps
                if mr <= i:  # If we can't move further
                    return -1
        
        return -1  # If we exit the loop without having reached the end



            

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minJumps(Arr,n)
		print(ans)
# } Driver Code Ends