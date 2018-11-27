#问题：
#合并两个有序链表l1和l2至一个新链表l
#Input:
#l1 = 1 -> 2 -> 4
#l2 = 1 -> 3 -> 4
#Output:l = 1 -> 1 -> 2 -> 3 -> 4 -> 4

#我的思路：
#比较l1.val和l2.val，按大小添加至l中
#有一个链表遍历完时，直接将另一个链表剩余添加至l中

#递归

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def print(self):
        while self:
            print(self.val)
            self = self.next
        #return ('%s' % (self.val))

#我的方法
class Solution:
    def mergeTwoLists(self, l1, l2):
        head = current = ListNode(0)
        if ((l1 == None) or (l2 == None)):
            return l2 or l1
        else:
            while (l1 and l2):
                if (l1.val >= l2.val):
                    current.next = l2
                    l2 = l2.next
                else:
                    current.next = l1
                    l1 = l1.next
                current = current.next
            if l1:
                current.next = l1
            if l2:
                current.next = l2
        return head.next

#递归方法
class solution_other():
    def mergeTwoList1(self, l1, l2):
        if ((l1 == None) or (l2 == None)):
            return l2 or l1
        if((l1.val >= l2.val)):
            l2.next = self.mergeTwoList1(l1, l2.next)
            return l2
        else:
            l1.next = self.mergeTwoList1(l1.next, l2)
            return l1

if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    s = Solution()
    result = s.mergeTwoLists(l1, l2)
    print('result:')
    ListNode.print(result)

    l1_new = ListNode(1)
    l1_new.next = ListNode(2)
    l1_new.next.next = ListNode(4)
    l2_new = ListNode(1)
    l2_new.next = ListNode(3)
    l2_new.next.next = ListNode(4)

    S = solution_other()
    result_new = S.mergeTwoList1(l1_new, l2_new)
    print('result_new:')
    ListNode.print(result_new)





