class Solution:
    def findDuplicates(self, arr):
        # Dictionary to store the frequency of elements
        frequency = {}
        for num in arr:
            frequency[num] = frequency.get(num, 0) + 1
        
        # Find elements with frequency > 1
        duplicates = [num for num, count in frequency.items() if count > 1]
        
        # Return duplicates in sorted order
        return sorted(duplicates)




#{ 
 # Driver Code Starts
# Initial Template for Python 3

t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().findDuplicates(arr)  # find the duplicates

    # Output formatting
    if s:
        print(" ".join(map(str, s)))  # Print duplicates in ascending order
    else:
        print("[]")  # Print empty list if no duplicates are found
    print("~")

# } Driver Code Ends