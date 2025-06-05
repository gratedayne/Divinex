class OutfitChanger:
    def __init__(self, character_name):
        self.character_name = character_name
        self.current_outfit = "default"

    def change_outfit(self, new_outfit):
        print(f"{self.character_name} is now wearing {new_outfit}.")
        self.current_outfit = new_outfit

    def get_outfit(self):
        return self.current_outfit