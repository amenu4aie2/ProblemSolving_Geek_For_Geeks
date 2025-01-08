#User function Template for python3

class Solution:
    #Function to count the number of possible triangles.
    def countTriangles(self, arr):
        arr.sort()
        n = len(arr)
        count = 0
    
        # Fix the largest side of the triangle
        for k in range(2, n):
            i, j = 0, k - 1
            while i < j:
                # Check if arr[i] + arr[j] > arr[k]
                if arr[i] + arr[j] > arr[k]:
                    # All pairs (i, j), (i+1, j), ..., (j-1, j) are valid
                    count += (j - i)
                    j -= 1  # Move the `j` pointer
                else:
                    i += 1  # Move the `i` pointer
        return count



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.countTriangles(arr))

        print("~")

# } Driver Code Ends