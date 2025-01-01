#User function Template for python3


class Solution:

    def anagrams(self, arr):
        """
        arr: list of words
        return: list of groups of anagrams (each group sorted lexicographically)
        """
        from collections import defaultdict

        # Dictionary to group words by their sorted form
        anagram_groups = defaultdict(list)

        for word in arr:
            # Sort the word to create a key for anagrams
            sorted_word = ''.join(sorted(word))
            anagram_groups[sorted_word].append(word)

        # Extract groups and sort each group lexicographically
        result = [group for group in anagram_groups.values()]

        # Return the result
        return result



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for tcs in range(t):
        words = input().split()

        ob = Solution()
        ans = ob.anagrams(words)

        for grp in sorted(ans):
            for word in grp:
                print(word, end=' ')
            print()

        print("~")

# } Driver Code Ends