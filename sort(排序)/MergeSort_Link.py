# Definition for singly-linked list.
from re import L, T
from tkinter import N


class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

"""
归并排序的链表实现
"""
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next ==None:  #head链表中只有一个节点或者为空
            return head
        #找到中点进行切割，快慢双指针法
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #无论head是单还是双，slow指向的都是左边链表的最后一个元素
        #进行分割
        left = head
        right = slow.next
        slow.next = None
        #递归进行划分
        left = self.sortList(left)
        right = self.sortList(right)
        #进行合并
        head = self.merge(left, right)        
        return head
    def merge(self,left, right):
        pre = ListNode(-1)
        h = pre
        while left and right:
            if left.val <= right.val:
                h.next = left
                h = h.next
                left = left.next
            else:
                h.next = right
                h = h.next
                right = right.next
        if left:
            h.next = left
        if right:
            h.next = right
        return pre.next

if __name__=='__main__':
    node1 = ListNode(4)  
    node2 = ListNode(3)  
    node3 = ListNode(2)  
    node4 = ListNode(1)  
    
    node1.next = node2  
    node2.next = node3  
    node3.next = node4  
    
    s = Solution()  
    result = s.sortList(node1)  
    
    while (result != None):  
        print(result.val)  
        result = result.next 
    