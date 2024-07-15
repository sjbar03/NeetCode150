class Solution():

    def search(self, nums, target) -> int:
        
        def split(l, r):
            if r - l <= 1:
                if nums[l] == target:
                    return l
                else:
                    return -1
            
            m = (r + l) // 2

            if nums[m] > target:

                return split(l, m)

            elif nums[m] <= target:

                return split(m, r)

        l,r = 0, len(nums)

        return split(l, r)

a = Solution()

tl = [1,2,3,4,5,6]
assert a.search(tl, 4) == 3
assert a.search(tl, 1) == 0
assert a.search(tl, 6) == 5

