class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = set()      # Stores characters in the current window
        i = 0           # Left pointer
        maxi = 0

        for j in range(len(s)):   # Right pointer expands the window

            # If current character is already in the window,
            # shrink the window from the left until it is removed.
            while s[j] in st:
                st.remove(s[i])
                i += 1

            # Add the current character
            st.add(s[j])

            # Update the maximum window size
            maxi = max(maxi, j - i + 1)

        return maxi