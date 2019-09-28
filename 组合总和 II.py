class Solution:
    def combinationSum2(self, candidates):
        candidates.sort()
        n = len(candidates)
        result = []

        def bt(i, temp_sum, temp):

            if temp_sum == target:
                result.append(temp)
                return
            if i == n or sum(temp) > target:
                return

            for j in range(i, n):

                if temp_sum + candidates[j] > target:
                    break

                # j>i 判断是在同一层 j=i可能在同一层
                if j > i and candidates[j] == candidates[j - 1]:
                    continue

                bt(j + 1, temp_sum + candidates[j], temp + [candidates[j]])

        bt(0, 0, [])
        return result
