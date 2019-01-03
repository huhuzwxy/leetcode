# 给定一个排好序的链表，删除重复元素，
# Input: 1->1->2->3->3
# Output: 1->2->3

# 思路：
# 两个指针。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def print(self):
        while self:
            print(self.val)
            self = self.next

class Solution:
    def deleteDuplicates(self, head):
        p = head
        q = p.next
        while q.next:
            if q.val == p.val:
                q = q.next
                p.next = q
                p = p.next
                q = q.next
            else:
                p = p.next
                q = q.next
        if p.val == q.val:
            p.next = None
        return head


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(3)

    s = Solution()
    result = s.deleteDuplicates(head)
    ListNode.print(result)