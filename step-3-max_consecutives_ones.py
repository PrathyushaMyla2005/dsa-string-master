"""
🔁 Problem: Max Consecutive Ones III (LeetCode #1004)  
🔗 Link: https://leetcode.com/problems/max-consecutive-ones-iii/

📌 Description:
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

👨‍💻 Author: Myla Prathyusha
💡 Topic: Sliding Window, Two Pointers  
🧠 Level: Medium  
🏢 Asked in: Google, Facebook, Amazon

---
Example 1:
Input:  nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2  
Output: 6  
Explanation: Flip 2 zeros at indices 5 and 10 to get 6 consecutive 1s.

Example 2:
Input:  nums = [0,0,1,1,1,0,0], k = 0  
Output: 3  

---

🕒 Time Complexity: O(n)  
    - Each element is visited at most twice by left and right pointers.

📦 Space Complexity: O(1)  
    - No extra space used other than a few variables.

🔄 Tags: Sliding Window, Two Pointers, Arrays
"""


"""
        Returns the length of the longest subarray with at most k 0s flipped to 1s.

        :param nums: List[int] - binary input array
        :param k: int - maximum number of 0s we can flip
        :return: int - maximum consecutive 1s after flipping at most k zeros
        """
class Solution:
    def longestOnes(self, nums, k):
        # Initialize the left pointer of the window
        left = 0

        # This will store the maximum length of consecutive 1s found
        max_len = 0

        # This will count how many 0s are currently inside the window
        zeros = 0

        # Start the sliding window from left to right
        for right in range(len(nums)):

            # If the current number is 0, we may want to flip it → count it
            if nums[right] == 0:
                zeros += 1

            # If the number of 0s in the window is more than k, shrink the window
            while zeros > k:
                # If the number going out from the left is 0, update zero count
                if nums[left] == 0:
                    zeros -= 1
                # Move the left pointer to shrink the window
                left += 1

            # Update max_len if the current window is larger
            # right - left + 1 = current window size
            max_len = max(max_len, right - left + 1)

        # Return the largest window size found
        return max_len
 # Example usage
solution = Solution()
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
result = solution.longestOnes(nums, k)
print("Final Answer:", result)