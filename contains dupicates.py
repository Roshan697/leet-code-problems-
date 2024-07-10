class Solution:
    def containsDuplicates(self, nums: list[int]) -> bool:
        hashset = set()
        
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

solution = Solution()
print(solution.containsDuplicates([1, 2, 3, 4]))  # Output: False
print(solution.containsDuplicates([1, 2, 3, 1]))  # Output: True
