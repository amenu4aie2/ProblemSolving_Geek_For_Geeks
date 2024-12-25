#User function Template for python3
class Solution:
    def setMatrixZeroes(self, mat):
        
        n, m = len(mat), len(mat[0])
        isFirstRowZero = any(mat[0][j] == 0 for j in range(m))
        isFirstColZero = any(mat[i][0] == 0 for i in range(n))
    
        # Use the first row and column to mark rows and columns to be zeroed
        for i in range(1, n):
            for j in range(1, m):
                if mat[i][j] == 0:
                    mat[i][0] = 0
                    mat[0][j] = 0
    
        # Update the matrix using the markers
        for i in range(1, n):
            for j in range(1, m):
                if mat[i][0] == 0 or mat[0][j] == 0:
                    mat[i][j] = 0
    
        # Update the first row if needed
        if isFirstRowZero:
            for j in range(m):
                mat[0][j] = 0
    
        # Update the first column if needed
        if isFirstColZero:
            for i in range(n):
                mat[i][0] = 0
                            
                    
#{ 
 # Driver Code Starts
import sys

# Position this line where user code will be pasted.
if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split()

    idx = 0
    t = int(data[idx])
    idx += 1
    results = []

    for _ in range(t):
        n, m = map(int, data[idx:idx + 2])
        idx += 2
        arr = []
        for i in range(n):
            arr.append(list(map(int, data[idx:idx + m])))
            idx += m

        sol = Solution()
        sol.setMatrixZeroes(arr)

        for row in arr:
            results.append(" ".join(map(str, row)))

        results.append("~")

    sys.stdout.write("\n".join(results) + "\n")

# } Driver Code Ends