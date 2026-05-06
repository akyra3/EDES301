"""
user_menu.py

Handles terminal menu input for rogue and mood selection.
"""


class UserMenu:
    def __init__(self, rogues, moods):
        self.rogues = rogues
        self.moods = moods

    def get_user_preferences(self):
        print("\nChoose recommendation type:")
        print("1. Rogue only")
        print("2. Mood only")
        print("3. Rogue and mood")

        choice = input("Enter 1, 2, or 3: ").strip()

        rogue = None
        mood = None

        if choice in ["1", "3"]:
            rogue = self.get_rogue_selection()

        if choice in ["2", "3"]:
            mood = self.get_mood_selection()

        return rogue, mood

    def get_rogue_selection(self):
        print("\nAvailable rogues:")

        for index, rogue in enumerate(self.rogues, start=1):
            print(f"{index}. {rogue}")

        selection = input("Select a rogue by number: ").strip()
        return self._select_from_list(selection, self.rogues)

    def get_mood_selection(self):
        print("\nAvailable moods:")

        for index, mood in enumerate(self.moods, start=1):
            print(f"{index}. {mood}")

        selection = input("Select a mood by number: ").strip()
        return self._select_from_list(selection, self.moods)

    def _select_from_list(self, selection, options):
        try:
            index = int(selection) - 1

            if 0 <= index < len(options):
                return options[index]

        except ValueError:
            pass

        print("Invalid selection. Defaulting to no selection.")
        return None
