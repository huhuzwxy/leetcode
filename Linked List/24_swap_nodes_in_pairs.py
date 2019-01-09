# 给定一个链表,交换每两个相邻结点，返回链表。
# Input: 1->2->3->4
# Output: 2->1->4->3

# 思路：
# 以两个结点为一个处理单位。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def print(self):
        while self:
            print(self.val)
            self = self.next

class Solution:
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        new_head = head.next
        head.next = self.swapPairs(head.next.next)
        new_head.next = head
        return new_head

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)

    s = Solution()
    result = s.swapPairs(head)
    ListNode.print(result)

