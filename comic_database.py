"""
comic_database.py

Loads and stores the local Batman comic recommendation database.
"""

import json
from pathlib import Path


class ComicDatabase:
    def __init__(self, filename):
        self.filename = Path(filename)
        self.comics = []

    def load_comics(self):
        """Load comic data from the JSON database."""
        with open(self.filename, "r", encoding="utf-8") as file:
            self.comics = json.load(file)
        return self.comics

    def get_all_comics(self):
        """Return all comics in the database."""
        return self.comics

    def get_rogues(self):
        """Return a sorted list of all rogues in the database."""
        rogues = set()

        for comic in self.comics:
            for rogue in comic.get("rogues", []):
                rogues.add(rogue)

        return sorted(rogues)

    def get_moods(self):
        """Return a sorted list of all moods in the database."""
        moods = set()

        for comic in self.comics:
            for mood in comic.get("moods", []):
                moods.add(mood)

        return sorted(moods)
