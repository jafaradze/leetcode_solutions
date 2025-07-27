from typing import List

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        count = 0
        i = 0
        j = 0
        players.sort()
        trainers.sort()
        n = len(players)
        m = len(trainers)
        while i < n and j < m:
            if players[i] <= trainers[j]:
                count += 1
                i += 1
                j += 1
            else:
                j += 1
        return count