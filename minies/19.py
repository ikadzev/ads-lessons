MAX_CONST = 10 ** 4


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists):
        lists = [i for i in lists if i]  # gc
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        p = Pyro4Nodes(lists)
        print([i.val for i in p.main])
        ans = ListNode()
        x = ListNode()
        while p.main_len != 0:
            nipaa = p.pop_min()
            if ans.next:
                x.val = nipaa.val
                x.next = ListNode()
                x = x.next
            else:
                ans.val = nipaa.val
                ans.next = x
            if nipaa.next:
                nipaa = nipaa.next
                p.append(nipaa)

        x = ans.next
        k = 0
        while x.next:
            k += 1
            x = x.next
        final = ListNode(val=ans.val)
        x = ListNode()
        final.next = x
        for _ in range(k - 1):
            ans = ans.next
            x.val = ans.val
            x.next = ListNode()
            x = x.next
        ans = ans.next
        x.val = ans.val
        return final


class Pyro4Nodes:
    def __init__(self, array=None):
        self.main = []
        self.main_len = 0
        if array is not None:
            for i in array:
                self.append(i)

    def append(self, new):
        self.main.append(new)
        self.main_len += 1
        if len(self.main) != 1:
            n = self.main_len - 1
            while n != 0 and self.main[n].val < self.main[(n - (2 - n % 2)) // 2].val:
                swp = (n - (2 - n % 2)) // 2
                swap(self.main, n, swp)
                n = swp

    def pop_min(self):
        if self.main_len == 0:
            return None
        swap(self.main, 0, -1)
        ret = self.main.pop()
        self.main_len -= 1
        n = 0
        if self.main_len <= 1:
            return ret
        while n * 2 < self.main_len:
            nipaa = self.main[n].val  # value of n'th element
            first = self.main[n * 2 + 1].val if n * 2 + 1 < len(self.main) else MAX_CONST
            second = self.main[n * 2 + 2].val if n * 2 + 2 < len(self.main) else MAX_CONST

            if nipaa > first and nipaa > second:
                if first < second:
                    swap_bit = 1
                    swap(self.main, n, n * 2 + 1)
                else:
                    swap_bit = 2
                    swap(self.main, n, n * 2 + 2)
            elif first < nipaa:
                swap_bit = 1
                swap(self.main, n, n * 2 + 1)
            elif second < nipaa:
                swap_bit = 2
                swap(self.main, n, n * 2 + 2)
            else:
                break

            n *= 2
            n += swap_bit
        return ret


def swap(lst, f, s):
    lst[f], lst[s] = lst[s], lst[f]