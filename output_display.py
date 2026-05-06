"""
output_display.py

Formats and displays recommendations.
"""


class OutputDisplay:
    def show_title(self):
        print("\n==============================")
        print(" Gotham Guide")
        print(" Batman Comic Recommender")
        print("==============================")

    def show_recommendations(self, recommendations):
        print("\nRecommendation output:")

        if not recommendations:
            print("No recommendation found.")
            return

        for index, comic in enumerate(recommendations, start=1):
            print(f"\n{index}. {comic['title']}")
            print(f"   Creators: {comic['creators']}")
            print(f"   Reason: {comic['reason']}")

    def show_error(self, message):
        print(f"Error: {message}")
