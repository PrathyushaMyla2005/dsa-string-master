"""
📌 Problem: Longest Common Prefix (LeetCode #14)
-----------------------------------------------

🧠 Task:
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

📈 Time Complexity:
- O(S) where S is the sum of all characters in all strings

📦 Space Complexity:
- O(1) — only constant extra space used (excluding input/output)

🛠 Approach:
- Take the first string as the reference
- Loop through each character of the first string
- Check if all other strings have the same character at that index
- If not, return the prefix up to that point
"""
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Loop over the characters of the first word
        for i in range(len(strs[0])):
            char = strs[0][i]

            # Compare this character with the same position in all other strings
            for word in strs[1:]:
                # If index i is out of bounds or characters don't match, return the prefix so far
                if i >= len(word) or word[i] != char:
                    return strs[0][:i]

        # If all characters of the first word match in others
        return strs[0]


# ✅ Example Usage
if __name__ == "__main__":
    sol = Solution()
    print("Longest Common Prefix:", sol.longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"
    print("Longest Common Prefix:", sol.longestCommonPrefix(["dog", "racecar", "car"]))     # Output: ""
