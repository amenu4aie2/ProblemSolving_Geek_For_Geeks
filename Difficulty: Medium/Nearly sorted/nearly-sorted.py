#User function Template for python3
from heapq import heappop, heappush, heapify


class Solution:
    def nearlySorted(self, arr, k):
        n=len(arr)
        heap = arr[:k + 1]

    # using heapify to convert list
        # into heap(or min heap)
        heapify(heap)
    
        # "rem_elmnts_index" is index for remaining
        # elements in arr and "target_index" is
        # target index of for current minimum element
        # in Min Heap "heap".
        target_index = 0
    
        # here even if size=k then n will be n=k,so i<n works fine
        for rem_elmnts_index in range(k + 1, n):
            arr[target_index] = heappop(heap)
            heappush(heap, arr[rem_elmnts_index])
            target_index += 1
    
        while heap:
            arr[target_index] = heappop(heap)
            target_index += 1

#{ 
 # Driver Code Starts
# Initial Template for Python 3
# Position this line where user code will be pasted.
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        k = int(input())
        ob = Solution()
        ob.nearlySorted(arr, k)
        print(*arr)
        # print("~")
        t -= 1
# } Driver Code Ends