"""
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，
使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class Solution:
    def threeSum(self, nums: list) -> list:
        from bisect import bisect_left, bisect_right

        target = 0

        result = []

        length = len(nums)

        if length < 3:
            return result

        count = {}
        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1
        keys = list(count.keys())
        keys.sort()

        # for numbers in count, it's count can be divided into three situations.
        # condition: num1 + num2 + num3 = 0
        # situation one: 1
        # situation two: 2, -(2 * number) must be in count if meet condition
        # situation there: >= 3, it must be zero if meet condition.
        if 0 in keys and count[0] >= 3:
            result.append([0, 0, 0])

        begin = 0
        end = bisect_left(keys, target)
        # print(keys)
        # print(count)
        # print('a', begin, end)

        for i in range(begin, end):
            a = keys[i]
            if count[a] >= 2 and target - 2 * a in count:
                result.append([a, a, target - 2 * a])

            max_b = (target - a) // 2  # target-a is remaining
            min_b = target - a - keys[-1]  # target-a is remaining and can max be keys[-1]
            b_begin = max(i + 1, bisect_left(keys, min_b))
            b_end = bisect_right(keys, max_b)
            # print('b', b_begin, b_end)

            for j in range(b_begin, b_end):
                b = keys[j]
                c = target - a - b
                if c in count and b <= c:
                    if b < c or count[b] >= 2:
                        result.append([a, b, c])
        return result


s = Solution()
print(s.threeSum([3,0,-2,-1,1,2]))

