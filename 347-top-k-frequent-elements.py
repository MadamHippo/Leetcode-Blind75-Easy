class Solution:
    # https://leetcode.com/problems/top-k-frequent-elements/
    # The runtime of this solution is O(nlogn), The space complexity is O(n) where n is the number of elements in the input list.
    # This solution uses the collections.Counter class to count the frequency of each element in the list, and the most_common() method to get the top K most frequent elements in the list.
    # In summary, this solution is counting the occurrences of each element in the list by using a Counter and then it's getting the most k frequent elements by using the most_common method.


    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Use Counter to count the frequency of each element in the list
        count = Counter(nums)
        # Get the k most common elements
        return [i[0] for i in count.most_common(k)]
