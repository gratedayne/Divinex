# silks/outfit_changer.py

class SilkForm:
    def __init__(self, character_name):
        self.character_name = character_name
        self.current_form = "Default Shroud"

    def change_form(self, new_form):
        self.current_form = new_form
        print(f"{self.character_name} now wears the {new_form}.")

    def view_form(self):
        return f"{self.character_name}'s current form: {self.current_form}"
