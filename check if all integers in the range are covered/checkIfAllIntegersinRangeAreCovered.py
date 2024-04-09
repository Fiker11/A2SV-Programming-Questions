class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges = sorted(ranges)
        start = left
        for row in range(len(ranges)):
            if ranges[row][0]<= start <= ranges[row][1]:
                if ranges[row][0]<= right <= ranges[row][1]:
                    return True
                else:
                    start = ranges[row][1] +1
        return False
            
