# offering_bowl/drop.py

class Drop:
    def __init__(self):
        self.pending_items = []

    def receive_item(self, item_name, source="system"):
        delivery = {
            "item": item_name,
            "source": source
        }
        self.pending_items.append(delivery)
        return f"New drop received from {source}: {item_name}"

    def collect_item(self):
        if not self.pending_items:
            return "No items to collect."
        item = self.pending_items.pop(0)
        return f"Collected: {item['item']} from {item['source']}"

    def view_pending(self):
        return [f"{d['item']} from {d['source']}" for d in self.pending_items]
