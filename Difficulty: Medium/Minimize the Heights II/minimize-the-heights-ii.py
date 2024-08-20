#User function Template for python3

class Solution:
    def getMinDiff(self, arr, n, k):
        arr.sort()
        
        largest=arr[-1]
        smallest=arr[0]
        ans=abs(largest-smallest)
        pivot=0
        for i in range(0,n-1):
            smallest=min(arr[0]+k,arr[i+1]-k)
            largest=max(arr[-1]-k,arr[i]+k)
            if(smallest<0):
                continue
            ans=min(ans,largest-smallest)
            
        
        
        return ans
        
            
            
            
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends