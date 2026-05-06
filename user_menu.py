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
        with open(self.filename, "r", encoding="utf-8") as file:
            self.comics = json.load(file)
        return self.comics

    def get_all_comics(self):
        return self.comics

    def get_rogues(self):
        rogues = set()
        for comic in self.comics:
            for rogue in comic.get("rogues", []):
                rogues.add(rogue)
        return sorted(rogues)

    def get_moods(self):
        moods = set()
        for comic in self.comics:
            for mood in comic.get("moods", []):
                moods.add(mood)
        return sorted(moods)
