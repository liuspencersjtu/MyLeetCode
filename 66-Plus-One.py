class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return [1]
        if digits[-1] < 9:
            return digits[:-1] + [digits[-1] + 1]
        else:
            return self.plusOne(digits[:-1]) + [0]
