class Solution:
    def subarrayXor(self, arr, k):
    # Initialize variables
        prefixXOR = 0
        count = 0
        prefixXORCount = {}
    
        for num in arr:
            # Update the prefix XOR
            prefixXOR ^= num
            
            # Check if prefixXOR itself equals k
            if prefixXOR == k:
                count += 1
    
            # Check if (prefixXOR ^ k) exists in the map
            target = prefixXOR ^ k
            if target in prefixXORCount:
                count += prefixXORCount[target]
    
            # Update the frequency of the current prefixXOR
            prefixXORCount[prefixXOR] = prefixXORCount.get(prefixXOR, 0) + 1
    
        return count


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    tc = int(input())

    for _ in range(tc):
        arr = list(map(int, input().split()))
        k = int(input())

        obj = Solution()
        print(obj.subarrayXor(arr, k))
        print("~")

# } Driver Code Ends