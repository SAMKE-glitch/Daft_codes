# Simulated data layer

class ItemRepository:
    def __init__(self):
        self.items = {
            1: {"name": "Laptop", "price": 1200.0},
            2: {"name": "Phone", "price": 800.0}
        }

    def get_item(self, item_id: int):
        return self.items.get(item_id, None)
