class Soh:
    def __init__(self, data):
        self.data = data
        self.next_soh = None

    def __repr__(self):
        return str(self.data)

class SohList:
    def __init__(self):
        self.lead = None
        self.num_sohs = 0
    
    def insert_s(self, data):
        self.num_sohs += 1
        new_soh = Soh(data)

        if self.lead is None:
            self.lead = new_soh
        else:
            new_soh.next_soh = self.lead
            self.lead = new_soh
    
    def insert_e(self, data):
        self.num_sohs += 1
        new_soh = Soh(data)

        if self.lead is None:
            self.lead = new_soh
        else:
            actual_soh = self.lead
            while actual_soh.next_soh is not None:
                actual_soh = actual_soh.next_soh
            actual_soh.next_soh = new_soh

    def traverse(self):
        actual_soh = self.lead
        while actual_soh is not None:
            print(actual_soh)
            actual_soh = actual_soh.next_soh

    def remove(self, data):
        if self.lead is None:
            return

        actual_soh = self.lead
        previous_node = None
        while actual_soh is not None and actual_soh.data != data:
            previous_node = actual_soh
            actual_soh = actual_soh.next_soh

        if previous_node is None:
            self.lead = actual_soh.next_soh
        else:
            previous_node.next_soh = actual_soh.next_soh


ss = SohList()
ss.insert_s(34)
ss.insert_s(31)
ss.insert_e(5)
print(ss.traverse())

