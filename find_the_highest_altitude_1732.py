from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest_alt = 0
        current_alt = 0
        for i in range(len(gain)):
            current_alt += gain[i]
            if current_alt >= highest_alt:
                highest_alt = current_alt

        return highest_alt