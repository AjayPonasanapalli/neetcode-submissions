class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while stones and len(stones) !=1:
            stones.sort()
            diff = stones[-1] - stones[-2]
            print(stones)
            if diff == 0:
                stones = stones[:-2]
            else:
                stones = stones[:-1]
                stones[-1] = diff

        return stones[0] if stones else 0    