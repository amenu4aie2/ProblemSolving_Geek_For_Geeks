#User function Template for python3
from collections import Counter
class Solution:
    def minIncrements(self, arr): 
        m=0
        a=Counter(arr)
        b=a.copy()
        for i,j in a.items():
            for x in range(1,j):
                while(True):
                    if(i+x not in b):
                        b[i+x]=1
                        m+=x
                        break
                    else:
                        x+=1
        return m
                        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    T = int(input())
    while T > 0:
        arr = [int(i) for i in input().split()]
        ob = Solution()
        print(ob.minIncrements(arr))

        T -= 1

# } Driver Code Ends