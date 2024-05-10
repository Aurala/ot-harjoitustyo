from rules.ruleset import Ruleset
from entities.universe import Universe


class CustomRuleset(Ruleset):

    def __init__(self):
        self.name = "B36/S23"
        self.friendly_name = "HighLife"
        self.description = "HighLife on Game of Life -variaatio ..."

    @classmethod
    def calculate(cls, universe: Universe):

        birth_conditions = [3, 6]
        survive_conditions = [2, 3]

        super().lifelike_calculate(universe, birth_conditions, survive_conditions)
