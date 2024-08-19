class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        current = []
        current_set = set()

        candidates.sort()

        def backtracking(i, total):

            if total == target:
                current_conv_val = "".join(str(x) for x in current.copy())
                if current_conv_val not in current_set:
                    current_set.add(current_conv_val)
                    res.append(current.copy())
                    return

            if i >= len(candidates):
                return
            if total < target:
                current.append(candidates[i])
                backtracking(i + 1, total + candidates[i])

                current.pop()
                backtracking(i + 1, total)

        backtracking(0, 0)

        return res
