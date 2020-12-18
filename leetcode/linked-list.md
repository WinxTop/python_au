+ [Reverse Linked List](#reverse-linked-list)
+ [Middle of the Linked List](#middle-of-the-linked-list)
+ [Palindrome Linked List](#palindrome-linked-list)
+ [Merge Two Sorted Lists](#merge-two-sorted-lists)
+ [Remove Nth Node From End of List](#remove-nth-node-from-end-of-list)
+ [Linked List Cycle](#linked-list-cycle)
+ [Intersection of Two Linked Lists](#intersection-of-two-linked-lists)
+ [Sort List](#sort-list)
+ [Reorder List](#reorder-list)
+ [Linked List Cycle II](#linked-list-cycle-ii)
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
## Reorder List
https://leetcode.com/problems/reorder-list/
```python
def reorderList(self, head: ListNode) -> None:
    if not head:
        return head
    a = []
    temp = head
    while(temp):
        a.append(temp)
        temp = temp.next
    temp = head
    i = 0
    n = len(a)//2
    m = -1
    n = 1
    o = -1
    for _ in range(len(a)-1):
        if o==1:
            temp.next = a[n]
            temp = temp.next
            o = -1
            n+=1
        else:
            temp.next = a[m]
            temp = temp.next
            o = 1
            m-=1
    temp.next = None
    return head
```
## Linked List Cycle II
https://leetcode.com/problems/linked-list-cycle-ii/
```python
def detectCycle(self, head: ListNode) -> ListNode:
    temp = head
    a = []
    while(temp):
        if temp not in a:
            a.append(temp)
        else:
            return temp
        temp = temp.next
    return None
```