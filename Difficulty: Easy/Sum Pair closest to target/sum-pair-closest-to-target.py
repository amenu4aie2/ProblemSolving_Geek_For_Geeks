#User function Template for python3
class Solution:
    def sumClosest(self, arr, target):
    # Sort the array to use two-pointer approach
        arr.sort()
        
        left, right = 0, len(arr) - 1
        closest_sum = float('inf')
        closest_pair = []
        
        # Variable to track the maximum absolute difference
        while left < right:
            current_sum = arr[left] + arr[right]
            
            # If the current sum is closer to the target, update closest_pair
            if abs(current_sum - target) < abs(closest_sum - target) or (abs(current_sum - target) == abs(closest_sum - target) and abs(arr[left] - arr[right]) > abs(closest_pair[0] - closest_pair[1])):
                closest_sum = current_sum
                closest_pair = [arr[left], arr[right]]
            
            # Adjust the pointers
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                break
        
        return closest_pair


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())
    while t > 0:
        arr = list(map(int, input().strip().split()))
        target = int(input().strip())
        ob = Solution()
        ans = ob.sumClosest(arr, target)
        if not ans:
            print("[]")
        else:
            print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends