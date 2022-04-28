class Record:
    def __init__(self, pname: str, cname: str, number_of_pax: int, cost_per_pax: int):
        self.package_name = pname
        self.customer_name = cname
        self.number_of_pax = number_of_pax
        self.cost_per_pax = cost_per_pax

    def __repr__(self):
        return f"Record(customer_name='{self.customer_name}', package_name='{self.package_name}', number_of_pax={self.number_of_pax}, cost_per_pax={self.cost_per_pax})"


class RecordNode:
    def __init__(self, data: Record):
        self.data = data
        self.next: RecordNode | None = None
