'''
we're given two linked lists,
1st one 2nd one
both of sorted and we have to merge them into an output linked list\
    the only catch we have to use the original nodes, we have to use original nondes
    we can't create copy of the nodes

Input: 1 -> 2 -> 4, 1 -> 3 -> 4
Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4

since, the list are sorted we can just start from the beginning of both of them compare the values, since both are 1, it
doesn't really matter which one we pick , so we just pick them and insert it to the output list head and move to the next one, and then compare 2 and 3.
Right now our output list is empty which gives us an edge case, so what we can do is create a dummy node. It is a pretty common technique
to avoid edge case of the initial empty list. Lets say we start with the lsit, its a dummy node so it can have any possible values, after inserting 1 we can compare
it with 2 and as 1 is still less than 2 we are going to insert it. We are going to insert it to our output list. Now we are going to compare 2 and 3, the value
is small is taken and inserted, then 3 , then we take the last value of list1 and compare it with 3 of list 2. In which we have to insert 3. Now, we are going to take
the least value and add it. 
We still have one more edge case to conquer, i.e, 
for list 1 there are no any more values left, so we can't really complete our algorithm.
Lucky for us there is only 1 value left in list 2 which is not always gonna be the case.
Maybe sometime there more than 1 value left in the 2nd or 1st list which ever comes last 
what we do in this case is we can take the remaining portion of the list. So, if we run out 1 of the list is empty
ofcourse the list 2 is still is sorted and we can litteraly take that portion and insert into our result.

'''

class mergeTwoSortedList:
    def mergeTwoLists(self, l1 : ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1: #if l1 is not null
            tail.next = l1
        elif l2:
            tail.next = l2

        return dummy.next