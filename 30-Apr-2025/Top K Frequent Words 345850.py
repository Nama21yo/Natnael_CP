# Problem: Top K Frequent Words - https://leetcode.com/problems/top-k-frequent-words/

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count_words = Counter(words)
        # max heap
        heap = [(-count, word) for word, count in count_words.items()]

        heapify(heap)

        return [heappop(heap)[1] for _ in range(k)]