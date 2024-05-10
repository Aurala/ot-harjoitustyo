from rules.ruleset import Ruleset
from entities.universe import Universe


class CustomRuleset(Ruleset):

    def __init__(self):
        self.name = "B3/S23"
        self.friendy_name = "Game of Life"
        self.description = "Alkuperäiset John Conway'n kehittämät säännöt"

    @classmethod
    def calculate(cls, universe: Universe):

        birth_conditions = [3]
        survive_conditions = [2, 3]

        super().lifelike_calculate(universe, birth_conditions, survive_conditions)
