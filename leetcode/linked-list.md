+ [Reverse Linked List](#reverse-linked-list)
+ [Middle of the Linked List](#middle-of-the-linked-list)
+ [Palindrome Linked List](#palindrome-linked-list)
+ [Merge Two Sorted Lists](#merge-two-sorted-lists)
+ [Remove Nth Node From End of List](#remove-nth-node-from-end-of-list)
+ [Linked List Cycle II](#linked-list-cycle-ii)
+ [Linked List Cycle](#linked-list-cycle)
+ [Reorder List](#reorder-list)
+ [Intersection of Two Linked Lists](#intersection-of-two-linked-lists)
+ [Sort List](#sort-list)
## Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/
```python
def reverseList(self, head: ListNode) -> ListNode:
	a = []
	temp = head
	if not temp:
		return None
	while(temp):
		a.append(temp.val)
		temp = temp.next
	a = a[::-1]
	head = ListNode(a[0])
	temp = head
	for i in range(1,len(a)):
		temp.next = ListNode(a[i])
		temp = temp.next
	return head
```
## Middle of the Linked List
https://leetcode.com/problems/middle-of-the-linked-list/
```python
def middleNode(self, head: ListNode) -> ListNode:
    count = 0
    temp = head
    while temp:
        count+=1
        temp = temp.next
    count = count // 2
    while count!=0:
        head = head.next
        count-=1
    return head
```
## Palindrome Linked List
https://leetcode.com/problems/palindrome-linked-list/
```python
def isPalindrome(self, head: ListNode) -> bool:
    sol = []
    cur = head
    while cur:
        sol.append(cur.val)
        cur = cur.next
    return sol == sol[::-1]
```
## Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/
```python
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(-1)
    prev = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            prev.next = l1
            l1 = l1.next
        else:
            prev.next = l2
            l2 = l2.next
        prev = prev.next
    prev.next = l1 or l2
    return dummy.next

```
## Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
```python
def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    fast=slow=head
    for i in range(n):
        fast=fast.next
    if not fast:return head.next
    while fast.next:
        slow=slow.next
        fast=fast.next
    slow.next=slow.next.next
    return head
```
## Linked List Cycle II
https://leetcode.com/problems/linked-list-cycle-ii/
```python
 detectCycle(self, head: ListNode) -> ListNode:
mp = head
= []
ile(temp):
f temp not in a:
a.append(temp)
lse:
return temp
emp = temp.next
turn None
```
## Linked List Cycle
https://leetcode.com/problems/linked-list-cycle/
```python
def hasCycle(self, head: ListNode) -> bool:
    slow = fast = head
    while(fast and fast.next):
        slow = slow.next
        fast = fast.next.next
        if(slow == fast):
            return True
    return False
```
## Reorder List
https://leetcode.com/problems/reorder-list/
```python
 reorderList(self, head: ListNode) -> None:
 not head:
eturn head
= []
mp = head
ile(temp):
.append(temp)
emp = temp.next
mp = head
= 0
= len(a)//2
= -1
= 1
= -1
r _ in range(len(a)-1):
f o==1:
temp.next = a[n]
temp = temp.next
o = -1
n+=1
lse:
temp.next = a[m]
temp = temp.next
o = 1
m-=1
mp.next = None
turn head
```
## Intersection of Two Linked Lists
https://leetcode.com/problems/intersection-of-two-linked-lists/
```python
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    temp1 = headA
    temp2 =headB
    d = {}
    while temp1:
        d[temp1] = temp1
        temp1 = temp1.next
    while temp2:
        if temp2 in d:
            return temp2
        temp2 = temp2.next
    return None
```
## Sort List
https://leetcode.com/problems/sort-list/
```python
def sortList(self, head: ListNode) -> ListNode:
    def mergeSort(head):
        if not head or not head.next :
            return head
        left = slow = fast = head
        fast = fast.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        right = slow.next
        slow.next = None
        left_sorted = mergeSort(left)
        right_sorted = mergeSort(right)
        return merge(left_sorted, right_sorted)
    def merge(l1, l2):
        dummy = ListNode(-1)
        prev = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        prev.next = l1 or l2
        return dummy.next
    return mergeSort(head)
```