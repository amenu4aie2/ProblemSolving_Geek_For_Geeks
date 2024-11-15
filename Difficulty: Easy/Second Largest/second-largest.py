#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        max1=-1
        max2=-1
        for i in arr:
            if(i>max1):
                max2=max1
                max1=i
                
            elif(i>max2 and i!=max1):
                max2=i
        return max2
                


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends