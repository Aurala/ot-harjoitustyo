"""
HighLife (B36/S23) on Game of Lifen variaatio.

John Conway totesi aikoinaan, että HighLife on
se peli, joka hänen olisi pitänyt löytää.

HighLife on erityisen mielenkiintoinen, koska
se mahdollistaa replikaattorin.
"""

from rules.ruleset import Ruleset
from entities.universe import Universe


class CustomRuleset(Ruleset):
    """Class containing a cellular automata ruleset.

    CustomRuleset inherits from Ruleset.

    Ruleset class has a method for performing computation
    for LifeLike cellular automata based on parameters
    defined in this class. If the user wants to implement
    more complex non-LifeLike rulesets, they will be done
    in a CustomRuleset class like this.

    After developing a CustomRuleset, it needs to be added
    to the configuration file.
    """

    def __init__(self):
        pass

    @classmethod
    def calculate(cls, universe: Universe):
        """Computes the next generation based on HighLife (B36/S23) rules.

        Args:
            universe (Universe): Object holding the data.
        """

        birth_conditions = [3, 6]
        survive_conditions = [2, 3]

        super().lifelike_calculate(universe, birth_conditions, survive_conditions)
