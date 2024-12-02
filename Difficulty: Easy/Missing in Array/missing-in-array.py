#User function Template for python3
class Solution:
    def missingNumber(self, arr):
        p=0
        for i in range(1,len(arr)+2):
            
            p^=i
        
        for i in arr:
            p^=i
        return p

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    arr = list(map(int, input().split()))
    s = Solution().missingNumber(arr)
    print(s)

    print("~")
# } Driver Code Ends