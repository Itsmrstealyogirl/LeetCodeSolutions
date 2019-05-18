# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None





# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         num1 = 0
#         num2 = 0
#         mult = 1
#         while(l1):
#             num1 += l1.val*mult
#             mult *= 10
#             l1 = l1.next
#         mult = 1
#         while(l2):
#             num2 += l2.val*mult
#             mult *= 10
#             l2 = l2.next
#         num3 = num1 + num2
#         head = ListNode(num3%10)
#         num3 = (num3 - num3%10)/10
#         temp = head
#         while(num3 != 0):
#             temp.next = ListNode(num3%10)
#             num3 = (num3 - num3%10)/10
#             temp = temp.next
#         return head
            
        

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum_num = (l1.val+l2.val)%10
        carry_over = int((l1.val+l2.val)/10)
        new_head = ListNode(sum_num)
        temp = new_head
        iter1 = l1.next
        iter2 = l2.next
        while(iter1 != None and iter2 != None):
            sum_ = (l1.val+l2.val+carry_over)%10
            carry_over = int((l1.val+l2.val+carry_over)/10)
            temp.next = ListNode(sum_)
            iter1 = iter1.next
            iter2 = iter2.next
        new_iter = None
        if(iter1 == None and iter2 == None):
            temp.next = ListNode(carry_over)
            return new_head
        elif(iter1 == None):
            new_iter = iter2
        else:
            new_iter = iter1
        while(new_iter != None):
            sum_ = (new_iter.val + carry_over)%10
            carry_over = int((new_iter.val + carry_over)/10)
            temp.next = ListNode(sum_)
        return new_head




