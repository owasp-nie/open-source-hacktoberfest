class Solution(object):
    def lengthOfLongestSubstring(self, s):
        charSet = set()
        l = 0
        length = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            length = max(length, len(charSet))
        return length

s = input("Enter the string you want longest substring of: ")

solution_instance = Solution()

print(solution_instance.lengthOfLongestSubstring(s))
