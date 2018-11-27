# 问题：
# 合并k个有序链表至一个新链表l
# Input: [1 -> 4 -> 5, 1 -> 3 -> 4, 2 -> 6]
# Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6

# 我的思路（分治策略）：
# 两两合并，类似归并排序。
# 实际中的问题：list与ListNode格式不统一的转换 -> 分割后list长度为1时，令list = list[0]，则为ListNode格式，可以直接用merge two sorted lists的算法。

# 其它方法：
# solution给了5个方法（包括归并），其它方法还未实现。

import math

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def print(self):
        while self:
            print(self.val)
            self = self.next
        #return ('%s' % (self.val))

class Solution:
    def mergetwo(self, l1, l2):
        if l1 == None or l2 == None:
            return l2 or l1
        if l1.val >= l2.val:
            l2.next = self.mergetwo(l1, l2.next)
            #ListNode.print(l1)
            return l2
        else:
            l1.next = self.mergetwo(l1.next, l2)
            #ListNode.print(l1)
            return l1
    def mergeKLists(self, lists):
        length = len(lists)
        if length <= 1:
            lists = lists[0]
            return lists
        mid = math.floor(length / 2)
        l1 = self.mergeKLists(lists[0 : mid])
        l2 = self.mergeKLists(lists[mid : ])
        return self.mergetwo(l1, l2)

if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(4)
    l1.next.next = ListNode(5)
    #ListNode.print(l1)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    #ListNode.print(l2)

    l3 = ListNode(2)
    l3.next = ListNode(6)
    #ListNode.print(l3)

    lists = [l1, l2, l3]
    S = Solution()
    result = S.mergeKLists(lists)
    print('result:')
    ListNode.print(result)
 
