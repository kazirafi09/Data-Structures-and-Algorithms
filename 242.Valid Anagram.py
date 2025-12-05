class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_table = {}
        if len(s) == len(t):
            for i in range(0, len(s)): 
                hash_table[s[i]] = hash_table.get(s[i], 0) + 1
                hash_table[t[i]] = hash_table.get(t[i], 0) - 1
            return all(v == 0 for v in hash_table.values())
        else:
            return False