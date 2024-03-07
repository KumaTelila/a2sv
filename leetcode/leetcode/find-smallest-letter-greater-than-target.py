class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low = 0
        high = len(letters) - 1
        if target == 'z':
            return letters[0]
        while low <= high:
            mid = low + (high - low)//2
            if target == letters[mid]:
                low = mid + 1
            elif target < letters[mid]:
                high = mid - 1
            else:
                low = mid  + 1
        if low == len(letters):
            return letters[0]
        return letters[low]
        