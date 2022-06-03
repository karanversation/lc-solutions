class Solution(object):
    def twoSum(self, nums, target):
        visited = {}
        for idx, n in enumerate(nums):
            if (target-n) in visited:
                return[idx, visited[target-n]]
            visited[n] = idx
        return -1
