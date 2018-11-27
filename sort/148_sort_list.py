#问题：
#将一个链表排序，时间复杂度为O(nlogn)，空间复杂度为0(1)
#Input: 4 -> 2 -> 1 -> 3
#Output:1 -> 2 -> 3 -> 4

#思路：
#时空复杂度决定所用排序方法为 归并排序
#利用快慢指针找链表中点
#快慢指针在链表中常用，（1）找链表中点（快一次走两步，慢一次走一步）（2）判断链表中是否有环（同1）（3）找链表中倒数第k个结点（快慢指针差k个结点）（4）单链表反转（快慢差1，每次都只走一步）

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
    def print(self):
        while self:
            print(self.val)
            self = self.next

class Solution:
    def sortList(self, head):
        if head == None or head.next == None:
            return head
        mid = self.findmid(head)
        l1 = head
        l2 = mid.next
        mid.next = None
        #注意设置mid.next = None,不然l1为整个链表，将中点后设置为空。
        l1 = self.sortList(l1)
        l2 = self.sortList(l2)
        return self.mergesort(l1, l2)

    #快慢指针找链表中点或者判断链表是否有环，一个一次走一步，一个一次走两步。
    def findmid(self, head):
        #链表为空或只有一个时直接返回
        if head == None or head.next == None:
            return head
        slow = head
        fast = head
        #链表值有两个时，slow指向第一个，直接找到中点
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def mergesort(self, l1, l2):
        heada = current = ListNode(0)
        if l1 == None or l2 == None:
            return l2 or l1
        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        if l1:
            current.next = l1
        else:
            current.next = l2
        return heada.next

if __name__ == '__main__':
    a = ListNode(4)
    a.next = ListNode(2)
    a.next.next = ListNode(1)
    a.next.next.next = ListNode(3)
    ListNode.print(a)

    s = Solution()
    result = s.sortList(a)
    ListNode.print(result)