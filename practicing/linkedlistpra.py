class N:
    def __init__(self, data):
        self.data = data
        self.nn = None

    def __repr__(self):
        return str(self.data)


class Ls:
    def __init__(self):
        self.head = None
        self.entries = 0

    def num_entries(self):
        print(str(self.entries))

    def ins_s(self, data):
        self.entries += 1
        new_n = N(data)

        if self.head is None:
            self.head = new_n
        else:
            new_n.nn = self.head
            self.head = new_n

    def ins_e(self, data):
        self.entries += 1
        new_n = N(data)

        if self.head is None:
            self.head = new_n
        else:
            n = self.head
            while n.nn is not None:
                n = n.nn
            n.nn = new_n
            new_n.nn = None


    def traverse(self):
        n = self.head

        while n is not None:
            print(n)
            n = n.nn

    def remove(self, data):
        if self.head is None:
            return 
        cur_n = self.head
        prev_n = None
        while cur_n is not None and cur_n.data != data:
            prev_n = cur_n
            cur_n = cur_n.nn
        if cur_n is None:
            return
        if prev_n is None:
            self.head = cur_n.nn
        else:
            prev_n.nn = cur_n.nn

        

if __name__ == '__main__':
    ls = Ls()

    
    ls.ins_s(10)
    ls.ins_s(9)
    ls.ins_s('adam')
    ls.ins_s('hello')
    ls.remove('hello')
    ls.remove('dfasdf')
    ls.traverse()