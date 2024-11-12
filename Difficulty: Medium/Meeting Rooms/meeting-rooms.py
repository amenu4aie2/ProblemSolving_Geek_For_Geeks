#User function Template for python3
class Solution:
    def canAttend(self,arr):
    # Sort meetings by start time
        arr.sort(key=lambda x: x[0])
        
        # Iterate through sorted meetings and check for overlaps
        for i in range(1, len(arr)):
            # If the start time of the current meeting is less than the end time of the previous meeting
            if arr[i][0] < arr[i - 1][1]:
                return False  # Overlap found
        
        return True  # No overlaps, all meetings can be attended
#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        # a = list(map(int, input().strip().split()))
        arr = []
        # j = 0
        for i in range(n):
            a = list(map(int, input().strip().split()))
            x = a[0]
            # j += 1
            y = a[1]
            # j += 1
            arr.append([x, y])
        obj = Solution()
        ans = obj.canAttend(arr)
        if ans:
            print("true")
        else:
            print("false")

# } Driver Code Ends