#User function Template for python3


class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def areAnagrams(self, s1, s2):
        dict1={}
        for i in s1:
            if i in dict1:
                dict1[i]+=1
            else:
                dict1[i]=1
        for  i in s2:
            if(i in dict1 and dict1[i]>0):
                dict1[i]-=1
            else:
                return False
            
        return True if (any(dict1.values())==False)  else False

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a = input().strip()
        b = input().strip()
        if (Solution().areAnagrams(a, b)):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends