class Nod:
    def __init__(self, data):
        self.data = data
        self.next_nod = None
    
    def __repr__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None
        self.num_of_nods = 0
    
    def ins_s(self, data):
        self.num_of_nods += 0
        new_nod = Nod(data)
        if self.head is None:
            self.head = new_nod
        else:
            new_nod.next_nod = self.head
            self.head = new_nod
    
    def rm(self, data):
        pointy_nod = self.head
        previous_nod = None
        if self.head is None:
            return 

        while pointy_nod.next_nod is not None and pointy_nod.data != data:
            previous_nod = pointy_nod
            pointy_nod = pointy_nod.next_nod
        
        # first node is the one we want to remove so O(1) complexity yay
        if previous_nod is None:
            self.head = pointy_nod.next_nod  
        else:
            # eh, O(n)
            previous_nod.next_nod = pointy_nod.next_nod

    def traverse(self):
        pointy_nod = self.head
        while pointy_nod is not None:
            print(pointy_nod)
            pointy_nod = pointy_nod.next_nod


ll = LinkedList()
ll.ins_s(123)
ll.ins_s(12)
ll.ins_s(1)
ll.rm(1)
ll.traverse()


        
        
        
