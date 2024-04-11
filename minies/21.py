from numpy import inf


class BinomialHeap:
    class Head:
        def __init__(self, value):
            self.value = value
            self.kids = []
            self.upper = None
            self.prio = 0

    def __init__(self, array=None, head=None):
        self.heads = dict()
        self.min = None
        if array:
            for val in array:
                self.insert(val)
        if head:
            if isinstance(head, BinomialHeap.Head):
                self.heads[head.prio] = head
            else:
                for h in head:
                    self.heads[h.prio] = h

    def insert(self, value):
        v_head = self.Head(value)
        if not self.min or value < self.min.value:
            self.min = v_head
        self.merge(BinomialHeap(head=v_head))
        return

    def peek_min(self):
        return self.min.value

    def peek_min_head(self):
        return self.min

    def extract_min(self):
        mini = self.min
        self.heads[mini.prio] = None
        if mini.kids:
            pyro = BinomialHeap(head=mini.kids)
            self.merge(pyro)
        self.min = self._seek_min()
        return mini.value

    def _seek_min(self):
        hd = [i for i in self.heads.values() if i]
        vl = [i.value for i in hd]
        mini = inf
        m_i = hd[0]
        for i in range(len(vl)):
            if vl[i] < mini:
                mini = vl[i]
                m_i = hd[i]
        return m_i

    def decrease_key(self, head: Head, k) -> None:
        head.value = k
        while head.upper and head.value < head.upper.value:
            temp = head.value
            head.value = head.upper.value
            head.upper.value = temp
            head = head.upper

    def delete(self, h: Head):
        while h.kids:
            h = h.kids[0]
        self.decrease_key(h, -inf)
        self.extract_min()
        return

    def _merge_heads(self, head1, head2):
        if head1.value > head2.value:
            head2.prio += 1
            head2.kids.append(head1)
            head1.upper = head2
            return head2
        else:
            head1.prio += 1
            head1.kids.append(head2)
            head2.upper = head1
            return head1

    def merge(self, p):
        carry = None
        new = BinomialHeap()
        for i in range(max(len(self.heads), len(p.heads)) + 1):
            try:
                p1 = self.heads[i]
            except KeyError:
                p1 = None
            try:
                p2 = p.heads[i]
            except KeyError:
                p2 = None
            if p1 and p2 and carry:
                new.heads[i] = carry
                carry = self._merge_heads(p1, p2)
            elif p1 and p2:
                carry = self._merge_heads(p1, p2)
                new.heads[i] = None
            elif p1 and carry:
                carry = self._merge_heads(p1, carry)
                new.heads[i] = None
            elif p2 and carry:
                new.heads[i] = None
                carry = self._merge_heads(p2, carry)
            elif p1:
                new.heads[i] = p1
            elif p2:
                new.heads[i] = p2
            else:
                new.heads[i] = carry
                carry = None
        for key, value in new.heads.items():
            self.heads[key] = value
        return


пирамида = BinomialHeap([11, 9, 7, 5, 3, 1, 2, 4, 6, 8, 10])
print(пирамида.extract_min())
print(пирамида.peek_min())
пирамида.insert(1)
print(пирамида.peek_min())
for _ in range(10):
    print(пирамида.extract_min())
