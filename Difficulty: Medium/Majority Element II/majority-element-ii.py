class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        from collections import Counter
        a=[]
        for i,j in ((Counter(arr)).items()):
            if(j>(len(arr)//3)):
                
                a.append(i)
        return sorted(a)

#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        nums = list(map(int, s.split()))
        ob = Solution()
        ans = ob.findMajority(nums)
        if not ans:
            print("[]")
        else:
            print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()

# } Driver Code Ends