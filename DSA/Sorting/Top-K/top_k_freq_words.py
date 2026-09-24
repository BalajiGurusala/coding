'''
Top K Frequent Words
Given a list of words, return the k most frequent words. If there is a tie, the words 
with the same frequency should be returned in lexicographical order.

Input:
{
 "k": 2,
 "words": ["i", "love", "leetcode", "i", "love", "coding"]
}
Output:
["i", "love"]
Explanation:
"i" and "love" are the two most frequent words.

Input:
{
 "k": 3,
 "words": ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
}
Output:
["the", "is", "sunny"]
Explanation:
"the", "is", and "sunny" are the three most frequent words.
'''

'''
Use quick select to find the k most frequent words efficiently.
Time Complexity: O(n) on average for the quick select step, where n is the number of unique words.
Space Complexity: O(1) additional space for the quick select step, ignoring the space used for the input and output.
'''

from collections import Counter


def top_k_frequent_words_quick_select(k, words):
    from collections import Counter 
    import random
    count = Counter(words)
    unique_words = list(count.keys())

    def lomutos_partition(start, end, pivot_index):
        pivot_frequency = count[unique_words[pivot_index]]
        unique_words[pivot_index], unique_words[start] = unique_words[start], unique_words[pivot_index]
        left = start
        for right in range(left+1, end + 1):
            if count[unique_words[right]] > pivot_frequency or (count[unique_words[right]] == pivot_frequency and unique_words[right] < unique_words[start]):
                left += 1
                unique_words[left], unique_words[right] = unique_words[right], unique_words[left]
        unique_words[start], unique_words[left] = unique_words[left], unique_words[start]
        return left
    
    def quick_select(start, end, k):
        if start == end:
            return
        pivot_index = random.randint(start, end)
        pivot_index = lomutos_partition(start, end, pivot_index)
        if k-1 == pivot_index:
            return
        elif k-1 < pivot_index:
            quick_select(start, pivot_index - 1, k)
        else:
            quick_select(pivot_index + 1, end, k)

    quick_select(0, len(unique_words) - 1, k)
    return sorted(unique_words[:k], key=lambda x: (-count[x], x))

def top_k_frequent_words_sorting_quick_select_v2(k, words):
    class TopKFrequentWords:
        def __init__(self, word, frequency):
            self.word = word
            self.frequency = frequency

        def __gt__(self, other):
            if self.frequency == other.frequency:
                return self.word < other.word
            return self.frequency > other.frequency
        def __repr__(self):
            return f"TopKFrequentWords(word={self.word}, frequency={self.frequency})"

    hmap = {}
    for word in words:
        if word in hmap:
            hmap[word] += 1
        else:
            hmap[word] = 1

    unique_words = [TopKFrequentWords(word, freq) for word, freq in hmap.items()]

    #Quick Select on unique_words
    def lomutos_partition(start, end, pivot_index):
        pivot_frequency = unique_words[pivot_index].frequency
        unique_words[pivot_index], unique_words[start] = unique_words[start], unique_words[pivot_index]
        left = start
        for right in range(left+1, end + 1):
            if unique_words[right] > unique_words[start]:
                left += 1
                unique_words[left], unique_words[right] = unique_words[right], unique_words[left]
        unique_words[start], unique_words[left] = unique_words[left], unique_words[start]
        return left

    def quick_select(start, end, k):
        if start == end:
            return
        pivot_index = random.randint(start, end)
        pivot_index = lomutos_partition(start, end, pivot_index)
        if k-1 == pivot_index:
            return
        elif k-1 < pivot_index:
            quick_select(start, pivot_index - 1, k)
        else:
            quick_select(pivot_index + 1, end, k)

    import random
    quick_select(0, len(unique_words) - 1, k)
    top_k_words = [tw.word for tw in unique_words[:k]]
    return sorted(top_k_words, key=lambda x: (-hmap[x], x), reverse=False)

def top_k_frequent_words_minheap(k, words):
    import heapq
    from collections import Counter

    class TopKFrequentWords:
        def __init__(self, word, frequency):
            self.word = word
            self.frequency = frequency

        def __lt__(self, other):
            if self.frequency == other.frequency:
                return self.word > other.word
            return self.frequency < other.frequency
        def __repr__(self):
            return f"TopKFrequentWords(word={self.word}, frequency={self.frequency})"

    count = Counter(words)
    heap = []
    for word, freq in count.items():
        heapq.heappush(heap, TopKFrequentWords(word, freq))
        if len(heap) > k:
            heapq.heappop(heap)

    top_k_words = []
    while heap:
        top_k_words.append(heapq.heappop(heap).word)
    return top_k_words[::-1]


if __name__ == "__main__":
    k = 2
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    print(top_k_frequent_words_quick_select(k, words))
    print(top_k_frequent_words_sorting_quick_select_v2(k, words))
    print(top_k_frequent_words_minheap(k, words))

    k = 3
    words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
    print(top_k_frequent_words_quick_select(k, words))
    print(top_k_frequent_words_sorting_quick_select_v2(k, words))
    print(top_k_frequent_words_minheap(k, words))
    