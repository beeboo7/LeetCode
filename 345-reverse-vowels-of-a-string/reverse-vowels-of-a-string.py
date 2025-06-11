class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        vowels = set('aeiouAEIOU')
        s = list(s)  # Convert to list for easy character replacement

        # Step 1: Two pointers to find vowels from both ends
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and s[left] not in vowels:
                left += 1
            while left < right and s[right] not in vowels:
                right -= 1
            # Swap the vowels
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return ''.join(s)

            