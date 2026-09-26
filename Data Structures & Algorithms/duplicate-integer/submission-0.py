class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = []
        for n in nums:
            if n in counts:
                return True
                break
            else:
                counts.append(n)
        return False
        
        
