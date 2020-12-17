+ [Valid Anagram](#valid-anagram)
+ [Reverse String](#reverse-string)
+ [Reverse Vowels of a String](#reverse-vowels-of-a-string)
+ [Reverse Words in a String III](#reverse-words-in-a-string-iii)
+ [To Lower Case](#to-lower-case)
## Valid Anagram
https://leetcode.com/problems/valid-anagram/
```python
def isAnagram(self, s: str, t: str) -> bool:
    if sorted(s)==sorted(t):
        return True
    else:
        return False
```
## Reverse String
https://leetcode.com/problems/reverse-string/
```python
def reverseString(self, s: List[str]) -> None:
    left = 0
    right = len(s) - 1
    while(left <= right):
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
```
## Reverse Vowels of a String
https://leetcode.com/problems/reverse-vowels-of-a-string/
```python
def reverseVowels(self, s: str) -> str:
    a=set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
    i=0
    j=len(s)-1
    s=list(s)
    while i<j:
        if s[i] not in a:
            i+=1
        elif s[j] not in a:
            j-=1
        if s[i] in a and s[j] in a:
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
    return "".join(s)
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
## To Lower Case
https://leetcode.com/problems/to-lower-case/
```python
def toLowerCase(self, str: str) -> str:
    alphabet = {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e',
         'F': 'f', 'G': 'g', 'H': 'h', 'I': 'i', 'J': 'j',
         'K': 'k', 'L': 'l', 'M': 'm', 'N': 'n', 'O': 'o',
         'P': 'p', 'Q': 'q', 'R': 'r', 'S': 's', 'T': 't',
         'U': 'u', 'V': 'v', 'X': 'x', 'W': 'w', 'Y': 'y',
         'Z': 'z'}
    for char in str:
        if char in alphabet:
            str = str.replace(char, alphabet[char])
    return str
```