#User function Template for python3
class Solution:
    
    def findSplit(self, arr):
        # Return an array of possible answer, driver code will judge and return true or false based on
        # ls,rs=[for i in range(len(arr))]
        ls,rs=[0],[0]
        suma=sum(arr)
        
        for i in range(len(arr)):
            ls.append(ls[-1]+arr[i])
        for i in arr[::-1]:
            rs.append(rs[-1]+i)
        rs.reverse()
        i,j=0,len(arr)
        # print(rs,ls)
        while (i<j):
            if(ls[i]==rs[j]==(suma-(ls[i]+rs[j]))):
                # print(i,j)
                return ([i-1,j-1])
            elif(ls[i]<rs[j]):
                i+=1
            elif(ls[i]>rs[j]):
                j-=1
            else:
                i+=1
        

        return ([-1,-1])


#{ 
 # Driver Code Starts
# Initial Template for Python 3

# Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        arr = [int(x) for x in input().strip().split()]

        ob = Solution()
        result = ob.findSplit(arr)

        if (result == [-1, -1]) or len(result) != 2:
            print("false")
        else:
            sum1 = sum2 = sum3 = 0
            for i in range(len(arr)):
                if i <= result[0]:
                    sum1 += arr[i]
                elif i <= result[1]:
                    sum2 += arr[i]
                else:
                    sum3 += arr[i]

            if sum1 == sum2 == sum3:
                print("true")
            else:
                print("false")
        print("~")

# } Driver Code Ends