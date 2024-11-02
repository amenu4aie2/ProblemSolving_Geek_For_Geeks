#User function Template for python3

class Solution:
    def checkDuplicatesWithinK(self, arr, k):
        x=dict()
        for i in range(len(arr)):
            if(arr[i] in x and ((i-x[arr[i]][-1])<=k)):
                
                return True
                
            else:
                if(arr[i] in x ):
                    x[arr[i]].append(i)
                else:
                    
                    x[arr[i]]=[i]
        return False
    
#{ 
 # Driver Code Starts
# Initial Template for Python 3
# Position this line where user code will be pasted.
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        k = int(input())
        ob = Solution()
        res = ob.checkDuplicatesWithinK(arr, k)
        if res:
            print("true")
        else:
            print("false")
        # print(res)
        print("~")
        t -= 1
# } Driver Code Ends