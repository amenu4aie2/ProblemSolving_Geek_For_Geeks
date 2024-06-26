#User function Template for python3

class Solution:
    #Function to return list containing first n fibonacci numbers.
    def printFibb(self,n):
        # USING DP APPROACH
        if(n==2 or n==1):
            return [1]*n
        
        else:
            arr=[1]*2
            for i in range(n-2):
                arr.append(arr[-1]+arr[-2])
            return arr
                
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        
        n=int(input())
        res = Solution().printFibb(n)
        for i in range (len(res)):
            print (res[i], end = " ") 
        print()
# } Driver Code Ends