#User function Template for python3
from collections import Counter
class Solution:
    def minRepeats(self, s1, s2):
        c=1
        k=(len(s2)//len(s1))+len(s1)
        i=0
        s=s1
        while(i<k):
            if s.find(s2)!=-1:
                return c
            else:
                s+=s1
                c+=1
            i+=1
        return -1
                
            
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        A = input()
        B = input()

        ob = Solution()
        print(ob.minRepeats(A, B))

# } Driver Code Ends