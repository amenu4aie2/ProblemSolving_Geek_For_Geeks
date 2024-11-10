#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    # Function to return a list containing the union of the two arrays.
    def findUnion(self, a, b):
        y = []  # Resultant list for the union
        i, j = 0, 0  # Initialize pointers for both arrays

        # Traverse both arrays
        while i < len(a) and j < len(b):
            # If current element of a is smaller, add it and increment i
            if a[i] < b[j]:
                if not y or y[-1] != a[i]:  # Avoid duplicates
                    y.append(a[i])
                i += 1
            # If current element of b is smaller, add it and increment j
            elif a[i] > b[j]:
                if not y or y[-1] != b[j]:  # Avoid duplicates
                    y.append(b[j])
                j += 1
            # If elements are equal, add any one and move both pointers
            else:
                if not y or y[-1] != a[i]:  # Avoid duplicates
                    y.append(a[i])
                i += 1
                j += 1

        # Add remaining elements of a (if any)
        while i < len(a):
            if not y or y[-1] != a[i]:  # Avoid duplicates
                y.append(a[i])
            i += 1

        # Add remaining elements of b (if any)
        while j < len(b):
            if not y or y[-1] != b[j]:  # Avoid duplicates
                y.append(b[j])
            j += 1

        return y

        
#{ 
 # Driver Code Starts.
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        a = list(map(int, input().strip().split()))
        b = list(map(int, input().strip().split()))
        ob = Solution()
        li = ob.findUnion(a, b)
        for val in li:
            print(val, end=' ')
        print()
        print("~")
# } Driver Code Ends