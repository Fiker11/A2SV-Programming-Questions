class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        s= [(sqrt(x**2+y**2),x,y)for x,y in points]
        s.sort()
        return [[x,y] for _,x,y in s][:k]