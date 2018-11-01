class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
    def print(self):
        while self:
            print(self.val)
            self = self.next

class Solution:
    def insertionSortList(self, head):
        if head == None or head.next == None:
            return head
        root = ListNode(0)
        root.next = head
        current = head
        while current.next:
            if current.val <= current.next.val:
                current = current.next
            else:
                p = current.next
                q = root
                while q.next.val < p.val:
                    q = q.next
                current.next = p.next
                p.next = q.next
                q.next = p
        return root.next

if __name__ == '__main__':
    a = ListNode(4)
    a.next = ListNode(2)
    a.next.next = ListNode(1)
    a.next.next.next = ListNode(3)
    #ListNode.print(a)

    s = Solution()
    result = s.insertionSortList(a)
    ListNode.print(result)





