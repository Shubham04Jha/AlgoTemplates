import math

class SegmentTree:
    def __init__(self, nums):
        self.st_bigNumber = 10**20
        self.st_smallNumber = 10**-12
        self.dummy = self.st_smallNumber
        self.nums = nums
        self.st_tree = []
        self.shiftOfBoundaries = 0
        self.build_tree()

    def paddNeed(self, nl):
        """Calculate padding needed to make size a power of 2."""
        return 2**(math.ceil(math.log2(nl))) - nl

    def build_tree(self):
        """Build the segment tree."""
        nl = len(self.nums)
        self.nums.extend([self.dummy] * self.paddNeed(nl))
        self.shiftOfBoundaries = len(self.nums)
        self.st_tree = [None] * (len(self.nums))
        self.st_tree.extend(self.nums)
        st_start = len(self.nums) - 1
        
        for i in range(st_start, 0, -1):
            left = self.st_tree[2 * i] if 2 * i < len(self.st_tree) else self.dummy
            right = self.st_tree[2 * i + 1] if 2 * i + 1 < len(self.st_tree) else self.dummy
            self.st_tree[i] = max(left, right)

    def query_max(self, start, end):
        """Query the maximum value in the range [start, end]."""
        start += self.shiftOfBoundaries
        end += self.shiftOfBoundaries
        res = self.st_smallNumber
        
        while start <= end:
            if start % 2 == 1:
                res = max(res, self.st_tree[start])
                start += 1
            if end % 2 == 0:
                res = max(res, self.st_tree[end])
                end -= 1
            start //= 2
            end //= 2
            
        return res

# Test Cases
def run_tests():
    test_cases = [
        ([1, 3, 2, 7, 9, 11], 0, 5),  # Query the entire range
        ([1, 3, 2, 7, 9, 11], 1, 3),  # Query a middle range
        ([1, 3, 2, 7, 9, 11], 4, 5),  # Query the last two elements
        ([1, 3, 2, 7, 9, 11], 0, 2),  # Query the first three elements
        ([5, 5, 5, 5], 0, 3),          # All elements the same
        ([10, 20, 30, 40, 50], 0, 4),  # Ascending order
        ([50, 40, 30, 20, 10], 0, 4),  # Descending order
        ([3, 1, 4, 1, 5, 9, 2, 6], 0, 7),  # Random values
    ]

    for nums, start, end in test_cases:
        st = SegmentTree(nums)  # Build the segment tree
        result = st.query_max(start, end)
        print(f'Max from index {start} to {end} in {nums}: {result}')

run_tests()
