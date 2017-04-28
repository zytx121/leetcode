class Solution(object):
    def subsetsWithDup(self, nums):

        def _dfs(nums, idx, path, ret_list):
            c = nums[idx]
            ret_list.append([c] + path)
            for k in range(idx - 1, -1, -1):
                if k < idx - 1 and nums[k] == nums[k + 1]:
                    continue
                _dfs(nums, k, [c] + path, ret_list)

        ret_list, n = [], len(nums)
        nums.sort()
        for i in range(n):
            if i < n - 1 and nums[i] == nums[i + 1]:
                continue
            _dfs(nums, i, [], ret_list)
        ret_list.append([])
        return ret_list