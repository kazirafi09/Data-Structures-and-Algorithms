class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:    
        hash_map = {}
        for s in strs:
            arr = [0] * 26
            for char in s:
                arr[ord(char)-ord("a")] += 1
            key = "#".join(map(str, arr))
            if key in hash_map:
                hash_map[key].append(s)
            else:
                hash_map[key] = [s]
        return list(hash_map.values())
