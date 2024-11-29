#User function template for Python
class Solution:
    def myAtoi(self, s):
        
        s=s.strip()
        p=1
        if(s and s[0]=="-"):
            p=-1
            s=s[1:]
        x="0"

        
        for i in s:
            if(i.isdigit()):
                x+=i
            else:
                break
        a=(2**31)
        b=int(x)*p
        if(b>(a-1) or b<(-a)):
            return a-1 if(p>0) else p*a
        return b

        
                


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        ob = Solution()
        print(ob.myAtoi(s))
        print("~")

# } Driver Code Ends