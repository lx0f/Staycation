class Record:
    def __init__(self, pname, cname, pax, cost):
        self.package_name = pname
        self.customer_name = cname
        self.num_pax = pax
        self.cost_per_pax = cost


class RecordNode:
    def __init__(self, data: Record):
        self.data = data
        self.next: RecordNode | None = None


class RecordQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data: Record):
        new = RecordNode(data)
        if self.head is None:
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            self.tail = new

    def dequeue(self):
        result = self.head
        self.head = result.next
        return result
