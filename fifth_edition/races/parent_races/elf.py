"""Parent class for the Elf race"""

import fifth_edition.races.races as races
import fifth_edition.abilities as abilities
import fifth_edition.focuses as focuses
import fifth_edition.languages as languages

__author__ = "Grant Colasurdo"


class Elf(races.Race):
    def __init__(
            self,
    ):
        super().__init__(
            character=character,
            name="Elf",
            description="Elves are a magical people of otherworldly grace, living in the w orld but not entirely " +
                        "part of it. They live in places of ethereal beauty, in the midst o f ancient forests or " +
                        "in silvery spires glittering with faerie light, where soft music drifts through the air and " +
                        "gentle fragrances waft on the breeze. Elves love nature and magic, art and artistry, music " +
                        "and poetry, and the good things o f the world.",
            age_of_attainment=100,
            lifespan=750,
            min_height=4.75,
            max_height=6.25,
            base_speed=30,
            dark_sight=True,
            given_stats=[
                (abilities.level_up, "Dexterity"),
                (focuses.choose_focus, ["Natural Lore", "Seeing"]),
                (languages.add_language, "Elven", 3),
                (languages.add_language, "Common Tongue", 2)
            ],



        )
