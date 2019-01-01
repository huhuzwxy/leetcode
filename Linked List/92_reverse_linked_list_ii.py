# 链表从位置m到n处逆序，一步完成。
# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL

# 思路：
# p、q分别指向m、n处，逆序，拼接

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def print(self):
        while self:
            print(self.val)
            self = self.next

class Solution:
    def reverseBetween(self, head, m, n):
        p = q = head
        for i in range(m - 1):
            tmp1 = p
            p = p.next
            q = q.next
        for j in range(n - m + 1):
            q = q.next
        mid = self.reverse(p, q)
        tmp1.next = mid
        return head
    def reverse(self, p, q):
        if p == q or p.next == q:
            return p
        result = self.reverse(p.next, q)
        p.next.next = p
        p.next = q
        return result

if __name__ == '__main__':
    list = ListNode(1)
    list.next = ListNode(2)
    list.next.next = ListNode(3)
    list.next.next.next = ListNode(4)
    list.next.next.next.next = ListNode(5)
    m = 2
    n = 4
    s = Solution()
    result = s.reverseBetween(list, m, n)
    ListNode.print(result)

