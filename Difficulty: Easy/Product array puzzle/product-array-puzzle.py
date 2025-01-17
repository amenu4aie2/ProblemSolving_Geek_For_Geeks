#User function Template for python3

class Solution:
    def productExceptSelf(self, arr):
        #code here
        
        out = [1]
        
        for i in range(len(arr) - 1):
            out.append(out[i] * arr[i])
        
        
        for i in range(len(arr) - 2, -1, -1):
            out[i] = out[i] * arr[i + 1]
            arr[i] = arr[i] * arr[i + 1]
        
        return out


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):

        arr = [int(x) for x in input().split()]

        ans = Solution().productExceptSelf(arr)
        print(*ans)
        print("~")

# } Driver Code Ends