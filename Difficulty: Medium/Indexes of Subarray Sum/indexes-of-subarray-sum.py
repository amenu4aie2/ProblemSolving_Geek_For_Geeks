#User function Template for python3
class Solution: 
    def subArraySum(self, arr, target):
        for i in range(len(arr)):
            s=0
            for j in range(i,len(arr)):
                s+=arr[j]
                if(s==target):
                    return [i+1,j+1]
                elif(s>target):
                    break
        return [-1]
#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        d = int(input().strip())
        ob = Solution()
        result = ob.subArraySum(arr, d)
        print(" ".join(map(str,
                           result)))  # Print the result in the desired format
        tc -= 1
        print("~")

# } Driver Code Ends