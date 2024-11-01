#User function Template for python3

class Solution:
    def maxSum(self,arr):
        x=sorted(arr)
        y=[]
        
        for i in range(len(arr)):
            if(i%2==0):
                y.append(x.pop(0))
            else:
                y.append(x.pop())
        # print(y)
        s=0
        for i in range(len(y)):
            s+=abs(y[i%(len(y))]-y[(i+1)%len(y)])
        return s
            
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.maxSum(arr)  # Call maxSum method and store result in ans
        print(ans)  # Print the result
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends