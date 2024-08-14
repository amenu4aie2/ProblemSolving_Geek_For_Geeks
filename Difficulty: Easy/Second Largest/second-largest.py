#User function Template for python3
class Solution:
    def print2largest(self, arr):
        # Code Here
        l1,l2=float('-inf'),float('-inf')
        for i in arr:
            if(l1<i):
                l2=l1
                l1=i
            elif(l2<i and i!=l1):
                l2=i
                
            
        return l2 if l2!=float('-inf') else -1
                


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.print2largest(arr)
        print(ans)

# } Driver Code Ends