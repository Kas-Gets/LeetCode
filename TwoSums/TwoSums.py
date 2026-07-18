from typing import List

class Solution:
    # 1. We removed the hardcoded data from here so the function can accept inputs properly
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 2. Added the logic so it actually calculates the answer
        seen = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], index]
            seen[num] = index
        return []
    
    
sol = Solution()
output = sol.twoSum(nums=[2, 7, 11, 15], target=9)

print(output)  # This will print: [0, 1]