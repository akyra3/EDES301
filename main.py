"""
main.py

Main controller for the Gotham Guide Batman comic recommender.
"""

from pathlib import Path

from button_input import ButtonInput
from comic_database import ComicDatabase
from output_display import OutputDisplay
from recommendation_engine import RecommendationEngine
from user_menu import UserMenu


class MainController:
    def __init__(self):
        current_dir = Path(__file__).parent
        database_path = current_dir / "comics.json"

        self.database = ComicDatabase(database_path)
        self.display = OutputDisplay()
        self.button = ButtonInput(pin="P2_08", active_low=True)

    def run(self):
        self.display.show_title()

        try:
            comics = self.database.load_comics()
            engine = RecommendationEngine(comics)
            menu = UserMenu(
                rogues=self.database.get_rogues(),
                moods=self.database.get_moods()
            )

            self.button.setup()

            keep_running = True

            while keep_running:
                rogue, mood = menu.get_user_preferences()

                print("\nSelected preferences:")
                print(f"Rogue: {rogue if rogue else 'None'}")
                print(f"Mood: {mood if mood else 'None'}")

                self.button.wait_for_press()

                recommendations = engine.recommend(rogue=rogue, mood=mood)
                self.display.show_recommendations(recommendations)

                again = input("\nGenerate another recommendation? (y/n): ").strip().lower()
                keep_running = again == "y"

        except KeyboardInterrupt:
            print("\nProgram stopped by user.")

        finally:
            self.button.cleanup()
            print("\nGotham Guide shut down.")


if __name__ == "__main__":
    controller = MainController()
    controller.run()
