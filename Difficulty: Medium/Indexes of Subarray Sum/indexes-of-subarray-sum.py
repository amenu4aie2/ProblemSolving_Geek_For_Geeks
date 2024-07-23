#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s):
        if(n==1):
            if(arr[0]==s):
                return [n,n]
        if(n==2):
            if(arr[0]+arr[1]==s):
                return [1,2]
        # if(s==0 and s not in arr):
        #     return [-1]
        # if(s in arr):
        #     return [arr.index(s)+1,arr.index(s)+1]
        # x=[arr[0]]
        # for i in range(n-1):
        #     x.append(x[i]+arr[i+1])
        # for i in range(n):
        #     if(x[i]==s):
        #         return [1,i+1]
        #     if(((x[i])>s) and ((x[i]-s) in x)):
        #         return [x.index(x[i]-s)+2,i+1]
        # return [-1]
        
        i=1
        su = 0
        l=0
        r =0
        su+=arr[0]
        while i<n:
            
            if su==s:
                # if l>r:return [-1]
                return l+1,r+1
            su+=arr[i]
            r+=1
            i+=1
            while su > s and l<r:
                # print(su,l)
                su-=arr[l]
                l+=1
            if su==s:
                # if l>r:return [-1]
                return l+1,r+1
        
        return [-1]
            
            
            

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends