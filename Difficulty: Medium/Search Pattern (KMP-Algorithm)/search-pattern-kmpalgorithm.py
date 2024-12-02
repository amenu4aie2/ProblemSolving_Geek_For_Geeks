#User function Template for python3

class Solution:
    def search(self, pat, txt):
        base=txt[0:len(pat)]
        ind=[]
        for i in range(len(txt)-len(pat)+1):
            if(i!=0):
                base=base[1:]+txt[i+len(pat)-1]
            
            if(base==pat):
                ind.append(i)
            
        return ind
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        patt = input().strip()
        ob = Solution()
        ans = ob.search(patt, s)
        if len(ans) == 0:
            print("[]", end="")
        for value in ans:
            print(value, end=' ')
        print()

# } Driver Code Ends