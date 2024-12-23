from db import SessionLocal
from models.part import Part as DBPart
from models.bundle import Bundle as DBBundle

class Part:
    def __init__(self, name, stock=0):
        self.name = name
        self.stock = stock
        self.sub_parts = []

    def add_sub_part(self, part, quantity):
        self.sub_parts.append((part, quantity))

    def max_buildable(self):
        if not self.sub_parts:  # Base case: leaf part
            return self.stock

        max_count = float('inf')
        for sub_part, quantity_needed in self.sub_parts:
            max_count = min(max_count, sub_part.max_buildable() // quantity_needed)

        return max_count


def load_parts_from_db():
   
    db = SessionLocal()

   
    parts = {p.id: Part(p.name, stock=p.stock or 0) for p in db.query(DBPart).all()}

    
    for bundle in db.query(DBBundle).all():
        parent_part = parts[bundle.parent_id]
        child_part = parts[bundle.child_id]
        parent_part.add_sub_part(child_part, bundle.quantity_needed)

    db.close()
    return parts


if __name__ == "__main__":
    
    parts = load_parts_from_db()
    bike = next(p for p in parts.values() if p.name == "Bike")
    print(f"Maximum Bikes: {bike.max_buildable()}")
