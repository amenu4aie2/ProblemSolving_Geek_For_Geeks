# User function Template for python3

class Solution:
    # Complete this function
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,arr):
        s1,s2=[0]*len(arr),[0]*len(arr)
        s1[0]=arr[0]
        for i in range(1,len(arr)):
            s1[i]=arr[i]+s1[i-1]
        x=arr[::-1].copy()
        s2[0]=x[0]
        for i in range(1,len(x)):
            s2[i]=x[i]+s2[i-1]
        s2=s2[::-1]
        for i in range(len(arr)):
            if(s2[i]==s1[i]):
                return i+1
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.equilibriumPoint(arr))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends