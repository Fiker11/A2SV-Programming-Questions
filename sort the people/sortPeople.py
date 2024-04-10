class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        height_index = {}
        for i, height in enumerate(heights):
            height_index[height] = i

        
        sorted_heights = sorted(heights, reverse=True)

        
        sorted_names = []
        for height in sorted_heights:
            sorted_names.append(names[height_index[height]])

        return sorted_names