class Solution:
    def myAtoi(self, s: str) -> int:
        # Step 1: Remove leading/trailing whitespaces
        s = s.strip()
        
        # Edge case: Empty string
        if not s:
            return 0
        
        # Step 2: Handle optional sign
        sign = 1
        if s[0] in ('-', '+'):
            if s[0] == '-':
                sign = -1
            s = s[1:]
        
        # Step 3: Extract numeric portion
        result = 0
        for char in s:
            if char.isdigit():
                result = result * 10 + int(char)
            else:
                break
        
        # Step 4: Apply bounds for 32-bit signed integer
        INT_MAX = (2**31) - 1
        INT_MIN = -(2**31)
        
        result *= sign
        if result > INT_MAX:
            return INT_MAX
        if result < INT_MIN:
            return INT_MIN
        
        return result


        
                


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        ob = Solution()
        print(ob.myAtoi(s))
        print("~")

# } Driver Code Ends