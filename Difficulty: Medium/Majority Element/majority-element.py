#User function template for Python 3

from collections import Counter
class Solution:
    def majorityElement(self, A, N):
        a=sorted(Counter(A).items(),key= lambda x:x[1],reverse=True)
        return a[0][0] if a[0][1]>N//2 else -1
        
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends