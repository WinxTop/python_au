+ [Max Consecutive Ones](#max-consecutive-ones)
+ [Reshape the Matrix](#reshape-the-matrix)
+ [Image Smoother](#image-smoother)
+ [Flipping an Image](#flipping-an-image)
+ [Transpose Matrix](#transpose-matrix)
+ [Move Zeroes](#move-zeroes)
+ [Squares of a Sorted Array](#squares-of-a-sorted-array)
## Max Consecutive Ones
https://leetcode.com/problems/max-consecutive-ones/
```python
def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    res=0
    count=0
    for i in nums:
        if i==1:
            count+=1
        else:
            if count>res:
                res=count
            count=0
    return max(res,count)
```
## Reshape the Matrix
https://leetcode.com/problems/reshape-the-matrix/
```python
def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
    m,n = len(nums), len(nums[0])
    if m*n != r*c:
        return nums
    else:
        res = []
        x = 0
        while x < r:
            res.append([nums[(i+c*x)//n][(i+c*x)%n] for i in range(c)])
            x += 1
    return res
```
## Image Smoother
https://leetcode.com/problems/image-smoother/
```python
def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
    row, col = len(M), len(M[0])
    res = [[0]*col for i in range(row)]
    dirs = [[0,0],[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[-1,1],[1,-1]]
    for i in range(row):
        for j in range(col):
            temp = [M[i+m][j+n] for m,n in dirs if 0<=i+m<row and 0<=j+n<col]
            res[i][j] = sum(temp)//len(temp)
    return res
```
## Flipping an Image
https://leetcode.com/problems/flipping-an-image/
```python
def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
    for row in A:
        i,j=0,len(row)-1
        while i<=j:
            row[i] , row[j] , i , j = 1^row[j] , 1^row[i] , i+1 , j-1
    return A
```
## Transpose Matrix
https://leetcode.com/problems/transpose-matrix/
```python
def transpose(self, A: List[List[int]]) -> List[List[int]]:
    rows, cols = len(A[0]), len(A)
    singleRow, answer = [], []
    for i in range(rows):
        for j in range(cols):
            singleRow.append(A[j][i])
        answer.append(singleRow)
        singleRow = []
    return answer
```
## Move Zeroes
https://leetcode.com/problems/move-zeroes/
```python
def moveZeroes(self, nums):
    i, j = 0, 0
    while j < len(nums):
        while j < len(nums) and nums[j] == 0:
            j += 1
        if j < len(nums):
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1
```
## Squares of a Sorted Array
https://leetcode.com/problems/squares-of-a-sorted-array/
```python
def sortedSquares(self, A: List[int]) -> List[int]:
    for i in range(len(A)):
        A[i] = A[i]**2
    A.sort()
    return A
```