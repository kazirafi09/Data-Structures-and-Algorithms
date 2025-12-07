import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_table = {}
        for num in nums:
            if num in hash_table: 
                hash_table[num] += 1
            else:
                hash_table[num] = 1

        min_heap = []

        for num, freq in hash_table.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap, (freq, num))
            elif freq > min_heap[0][0]:
                heapq.heappushpop(min_heap, (freq, num))
        return [num for freq, num in min_heap]