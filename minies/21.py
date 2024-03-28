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
        if array:
            for val in array:
                self.insert(val)
        if head:
            self.heads[head.prio] = head

    def insert(self, value):
        if len(self.heads.values()) != 0:
            pyro = BinomialHeap()
            pyro.heads[0] = self.Head(value)
            self.merge(pyro)
        else:
            self.heads[0] = self.Head(value)
        return

    def peek_min(self):
        min_list = [i.value for i in self.heads.values() if i]
        return min(min_list)

    def peek_min_head(self):
        min_list = [i.value for i in self.heads.values() if i]
        mini = min(min_list)
        for i in range(len(self.heads)):
            if self.heads[i] and self.heads[i].value == mini:
                return self.heads[i]

    def extract_min(self):
        min_list = [i.value for i in self.heads.values() if i]
        mini = min(min_list)
        for i in range(len(self.heads)):
            if self.heads[i] and self.heads[i].value == mini:
                mini = self.heads[i]
                self.heads[i] = None
                break
        if mini.kids:
            for i in mini.kids:
                pyro = BinomialHeap(head=i)
                self.merge(pyro)
        return mini.value

    def decrease_key(self, head, k):
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


piramoid = BinomialHeap([11, 9, 7, 5, 3, 1, 2, 4, 6, 8, 10])
print(piramoid.extract_min())
print(piramoid.peek_min())
piramoid.insert(1)
print(piramoid.peek_min())
for i in range(10):
    print(piramoid.extract_min())
