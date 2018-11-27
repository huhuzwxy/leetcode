# 链表逆序
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL

# 思路：
# 递归

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def print(self):
        while self:
            print(self.val)
            self = self.next

class Solution:
    def reverseList(self, head):
        if head == None or head.next == None:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p

if __name__ == '__main__':
    list = ListNode(1)
    list.next = ListNode(2)
    list.next.next = ListNode(3)
    #ListNode.print(list)

    s = Solution()
    result = s.reverseList(list)
    ListNode.print(result)
