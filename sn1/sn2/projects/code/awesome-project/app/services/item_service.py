from app.repositories.item_repository import ItemRepository


class ItemService:
    def __init__(self):
        self.repo = ItemRepository()

    def fetch_item(self, item_id: int):
        item = self.repo.get_item(item_id)
        if not item:
            raise ValueError("Item not found")
        return item
