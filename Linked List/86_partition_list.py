# 给定一个链表和一个值x，将小于x的放在大于等于x的前面，不改变相对位置。
# Input: head = 1->4->3->2->5->2, x = 3
# Output: 1->2->2->4->3->5

# 思路：
# 先将小于x的放在x的前面，将x前的链表排序，前后拼接。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def print(self):
        while self:
            print(self.val)
            self = self.next

class Solution:
    def partition(self, head, x):
        p = head
        q = p.next
        while q.val != x:
            q = q.next
            p = p.next
        p.next = None
        tmp1 = q
        tmp_list = q.next
        while tmp_list != None:
            if tmp_list.val < x:
                p.next = tmp = tmp_list
                tmp_list = tmp_list.next
                tmp.next = None
                p = p.next
            else:
                q.next = tmp = tmp_list
                tmp_list = tmp_list.next
                tmp.next = None
                q = q.next
        head = self.sortList(head)
        tmp = head
        while tmp.next != None:
            tmp = tmp.next
        tmp.next = tmp1
        return head

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
    list = ListNode(1)
    list.next = ListNode(4)
    list.next.next = ListNode(3)
    list.next.next.next = ListNode(2)
    list.next.next.next.next = ListNode(5)
    list.next.next.next.next.next = ListNode(2)
    x = 3
    s = Solution()
    result = s.partition(list, x)
    ListNode.print(result)
