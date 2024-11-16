#User function Template for python3

class Solution:
	def pushZerosToEnd(self,arr):
	    
	   # ds - arr , ll , q ,d q
	   count=0
	   for i in range(len(arr)):
	       if(arr[i] != 0):
	                arr[count]=arr[i]
	                count+=1
	   for i in range(count,len(arr)):
	       arr[i]=0
	   
	        
	            
	    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
# } Driver Code Ends