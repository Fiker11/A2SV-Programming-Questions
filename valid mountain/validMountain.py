class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
            if len(arr) < 3:
                return False
            i = 0
            # Find the peak (increasing part)
            while i < len(arr) - 1 and arr[i] < arr[i + 1]:
                i += 1

            # Check if the peak is not at the beginning or end
            if i == 0 or i == len(arr) - 1:
                return False

            # Check for strictly decreasing part
            for j in range(i + 1, len(arr)):
                if arr[j] >= arr[j - 1]:
                    return False

            return True