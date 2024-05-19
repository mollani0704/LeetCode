class Solution(object):
    def topKFrequent(self, nums, k):
        # 두번째 풀이
        elements = {}
        for num in nums:
            elements[num] = elements.get(num, 0) + 1
        
        sorted_elements = sorted(elements.items(), key=lambda x : x[1], reverse=True)

        top_k = [item[0] for item in sorted_elements[:k]]
        return top_k
        
        # 첫번쨰 풀이
        # count = {}
        # freq = [[] for i in range(len(nums) + 1)]

        # for n in nums:
        #     count[n] = 1 + count.get(n, 0)
        # for n, c in count.items():
        #     freq[c].append(n)
        
        # result = []

        # for i in range(len(freq) - 1, 0, -1):
        #     for n in freq[i]:
        #         result.append(n)
        #         if len(result) == k:
        #             return result