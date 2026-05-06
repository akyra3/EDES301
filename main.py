"""
recommendation_engine.py

Contains the rule-based Batman comic recommendation logic.
"""


class RecommendationEngine:
    def __init__(self, comics):
        self.comics = comics

    def recommend(self, rogue=None, mood=None):
        rogue = rogue.strip().lower() if rogue else None
        mood = mood.strip().lower() if mood else None

        matches = []

        for comic in self.comics:
            comic_rogues = [r.lower() for r in comic.get("rogues", [])]
            comic_moods = [m.lower() for m in comic.get("moods", [])]

            rogue_match = rogue in comic_rogues if rogue else True
            mood_match = mood in comic_moods if mood else True

            if rogue_match and mood_match:
                matches.append(comic)

        if matches:
            return matches

        return self.fallback_recommendation(mood)

    def fallback_recommendation(self, mood=None):
        if mood:
            mood = mood.lower()
            mood_matches = [
                comic for comic in self.comics
                if mood in [m.lower() for m in comic.get("moods", [])]
            ]
            if mood_matches:
                return mood_matches

        # Final fallback if nothing matches.
        return [self.comics[0]] if self.comics else []
