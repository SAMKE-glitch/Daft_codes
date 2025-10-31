from sqlmodel import Session, select
from app.models.item_model import Item


class ItemRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_item(self, item_id: int):
        return self.session.get(Item, item_id)

    def create_item(self, item: Item):
        self.session.add(item)
        self.session.commit()
        self.session.refresh(item)

        return item
