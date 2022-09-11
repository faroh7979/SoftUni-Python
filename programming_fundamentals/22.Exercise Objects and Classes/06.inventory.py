class Inventory:
    def __init__(self, __capacity):
        self.capacity = __capacity
        self.items = []
        self.value_of_capacity = __capacity

    def add_item(self, item):
        if self.capacity > 0:
            self.items.append(item)
            self.capacity -= 1
        else:
            return 'not enough room in the inventory'

    def get_capacity(self):
        return self.value_of_capacity

    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {self.capacity}"


