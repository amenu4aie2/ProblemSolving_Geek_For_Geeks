#User function Template for python3
import numpy as np
def rotate(mat): 
    #code here
    mat.reverse()
    x=list(np.transpose(mat))
    for i in range(len(x)):
        for j in range(len(x)):
            mat[i][j]=x[i][j]
    
    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        matrix = []
        for i in range(N):
            arr = [int(x) for x in input().strip().split()]
            matrix.append(arr)

        rotate(matrix)
        for i in range(N):
            for j in range(N):
                print(matrix[i][j], end=' ')
            print()
        print("~")

# } Driver Code Ends