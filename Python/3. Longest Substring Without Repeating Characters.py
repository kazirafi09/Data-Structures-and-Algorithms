class Solution(object):
    def lengthOfLongestSubstring(self, s):
        non_repeating_character = set()
        l = 0
        r = 0
        longest_string_length = 0
        while r < len(s):
            if s[r] not in non_repeating_character:
                non_repeating_character.add(s[r])
                r += 1
                longest_string_length = max(r - l, longest_string_length)
            else:
                non_repeating_character.discard(s[l])
                l += 1
        return longest_string_length