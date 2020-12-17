+ [Reverse Integer](#reverse-integer)
+ [Palindrome Number](#palindrome-number)
+ [Fizz Buzz](#fizz-buzz)
+ [Base 7](#base-7)
+ [Fibonacci Number](#fibonacci-number)
+ [Largest Perimeter Triangle](#largest-perimeter-triangle)
+ [Sqrt(x)](#sqrtx)
## Reverse Integer
https://leetcode.com/problems/reverse-integer/
```python
def reverse(self, x: int) -> int:
    rev = int(str(abs(x))[::-1])
    i = -rev if x < 0 else rev
    if i < -2**31 or i > 2**31-1:
        return 0
    return i
```
## Palindrome Number
https://leetcode.com/problems/palindrome-number/
```python
def isPalindrome(self, x: int) -> bool:
    z = str(x)[::-1]
    if str(z) == str(x):
        return True
    else:
        return False
```
## Fizz Buzz
https://leetcode.com/problems/fizz-buzz/
```python
def fizzBuzz(self, n: int) -> List[str]:
    outPut = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            outPut.append('FizzBuzz')
        elif i % 5 == 0:
            outPut.append('Buzz')
        elif i % 3 == 0:
            outPut.append('Fizz')
        else:
            outPut.append(str(i))
    return outPut
```
## Base 7
https://leetcode.com/problems/base-7/
```python
def convertToBase7(self, num: int) -> str:
    if not num:
        return str(num)
    sign = '-' if num < 0 else ''
    num = abs(num)
    result = []
    while num:
        result.append(str(num % 7))
        num //= 7
    result.append(sign)
    return ''.join(reversed(result))
```
## Fibonacci Number
https://leetcode.com/problems/fibonacci-number/
```python
def fib(self, n: int) -> int:
    res = [0,1]
    c = 0
    if n == 0:
        return res[0]
    elif n==1:
        return res[1]
    for i in range(2,n+1):
        c = res[0] + res[1]
        res[0] = res[1]
        res[1] = c
    return res[-1]
```
## Largest Perimeter Triangle
https://leetcode.com/problems/largest-perimeter-triangle/
```python
def largestPerimeter(self, A: List[int]) -> int:
    A.sort()
    N = len(A)
    res = 0
    for i in range(N - 1, 1, -1):
        if A[i - 2] + A[i - 1] > A[i]:
            return A[i - 2] + A[i - 1] + A[i]
    return 0
```
## Sqrt(x)
https://leetcode.com/problems/sqrtx/
```python
def mySqrt(self, x: int) -> int:
    a = 0
    b = x
    i=1
    while i < 1000:
        mid = (a+b)/2
        if mid**2 < x:
            a = mid
        if mid**2 > x:
            b = mid
        i = i + 1
    check = int(math.floor(mid))
    if (check + 1)**2 == x:
        return int(check + 1)
    else:
        return int(math.floor(mid))
```