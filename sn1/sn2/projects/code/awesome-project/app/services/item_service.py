from app.repositories.item_repository import ItemRepository
from app.models.item_model import Item
from sqlmodel import Session


class ItemService:
    def __init__(self, session: Session):
        self.repo = ItemRepository(session)

    def fetch_item(self, item_id: int):
        item = self.repo.get_item(item_id)
        if not item:
            raise ValueError("Item not found")
        return item

    def create_item(self, item: Item):
        return self.repo.create_item(item)
