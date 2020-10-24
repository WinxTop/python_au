+ [Sqrt(x)](#sqrtx)
+ [Reverse Words in a String III](#reverse-words-in-a-string-iii)

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
## Reverse Words in a String III
https://leetcode.com/problems/reverse-words-in-a-string-iii/
```python
def reverseWords(self, s: str) -> str:
    s=s.split()
    for i in range(len(s)):
        s[i]=s[i][::-1]
    return " ".join(s)
```