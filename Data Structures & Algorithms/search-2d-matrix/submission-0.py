class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = [(matrix[i][0],i) for i in range(len(matrix))]
        l,r = 0,len(matrix) - 1
        while l<=r:
            mid = (l+r)//2
            if start[mid][0] == target:
                return True
            elif start[mid][0]<target:
                l= mid+1
            else:
                r = mid-1
        print(start[l-1])
        array = matrix[l-1]
        l,r = 0,len(array) - 1
        while l<=r:
            mid = (l+r)//2
            if array[mid] == target:
                return True
            elif array[mid]<target:
                l= mid+1
            else:
                r = mid-1
        return False
        