+ [Non-overlapping Intervals](#non-overlapping-intervals)
+ [Merge Intervals](#merge-intervals)
+ [Insert Interval](#insert-interval)
## Non-overlapping Intervals
https://leetcode.com/problems/non-overlapping-intervals/
```python
def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    if not intervals:
        return 0
    remove=0
    intervals=sorted(intervals, key=lambda x:x[1])
    startP=intervals[0][0]
    endP=intervals[0][1]
    for i in range(1,len(intervals)):
        startN=intervals[i][0]
        endN=intervals[i][1]
        if  startN<endP:
            remove+=1
        else:
            startP=startN
            endP=endN
    return remove
```
## Merge Intervals
https://leetcode.com/problems/merge-intervals/
```python
def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    res = []
    i = 0
    intervals.sort()
    while i < len(intervals):
        if not res: res.append(intervals[i])
        else:
            a_start, a_end = intervals[i]
            b_start, b_end = res[-1]
            if a_start <= b_end and b_start <= a_end: #overlap
                res[-1][0] = min(a_start, b_start)
                res[-1][1] = max(a_end, b_end)
            else:
                res.append(intervals[i])
        i += 1
    return res
```
## Insert Interval
https://leetcode.com/problems/insert-interval/
```python
def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
 intervals.append(newInterval)
 if len(intervals)==1:
  return intervals
 intervals.sort()
 res = [intervals[0]]
 for s in intervals[1:]:
  if s[0]<=res[-1][1]:
   res[-1][1] = max(res[-1][1], s[1])
  else:
   res.append(s)
 return res
```