+ [Sqrt(x)](#sqrtx)
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