#User function Template for python3



class Solution:
    def find3Numbers(self, arr):
        # prefix sum
        maxia=[-1]*len(arr)
        minima=[-1]*len(arr)
        minimum=0
        for i in range(1,len(arr)):
            if(arr[i]<=arr[minimum]):
                
                minimum=i
                
            else:
                minima[i]=minimum
        maximum=len(arr)-1
        for i in range(len(arr)-2,-1,-1):
            if(arr[i]>=arr[maximum]):
                
                maximum=i
                
            else:
                maxia[i]=maximum
        res=[]
        for i in range(len(arr)):
            if(maxia[i]!=-1 and minima[i]!=-1):
                
                res.append(arr[minima[i]])
                res.append(arr[i])
                res.append(arr[maxia[i]])
                return res

        return []
        
                
                

#{ 
 # Driver Code Starts
#Initial Template for Python 3


def isSubSequence(v1, v2):
    m = len(v2)
    n = len(v1)
    j = 0  # For index of v2
    # Traverse v1 and v2
    for i in range(n):
        if j < m and v1[i] == v2[j]:
            j += 1
    return j == m


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        n = len(arr)
        obj = Solution()
        res = obj.find3Numbers(arr)
        if len(res) != 0 and len(res) != 3:
            print(-1)
        else:
            if not res:
                print(0)
            elif res[0] < res[1] < res[2] and isSubSequence(arr, res):
                print(1)
            else:
                print(-1)

# } Driver Code Ends