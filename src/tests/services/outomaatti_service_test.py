import unittest
from config import settings
from services.outomaatti_service import OutomaattiService


class TestOutomaattiService(unittest.TestCase):

    blinker_vertical = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]
    blinker_horizontal = [[0, 0, 0], [1, 1, 1], [0, 0, 0]]

    def setUp(self):
        self.outomaatti = OutomaattiService()

    def test_create_service_with_default_parameters(self):
        self.assertEqual(self.outomaatti.get_universe_as_text(),
                         ".....\n.....\n.....\n.....\n.....\n")

    def test_create_service_with_universe_of_4x5(self):
        outomaatti = OutomaattiService(4, 5)
        self.assertEqual(outomaatti.get_universe_as_text(),
                         "....\n....\n....\n....\n....\n")

    def test_universe_dimensions(self):
        outomaatti = OutomaattiService(42, 69)
        self.assertEqual(outomaatti.get_width(), 42)
        self.assertEqual(outomaatti.get_height(), 69)

    def test_invert_cell_in_universe(self):
        outomaatti = OutomaattiService(1, 1)
        outomaatti.invert_cell(0, 0)
        self.assertEqual(outomaatti.get_universe_as_text(), "*\n")
        outomaatti.invert_cell(0, 0)
        self.assertEqual(outomaatti.get_universe_as_text(), ".\n")

    def test_add_cell_to_universe(self):
        outomaatti = OutomaattiService(1, 1)
        outomaatti.add_cell(0, 0)
        self.assertEqual(outomaatti.get_universe_as_text(), "*\n")

    def test_add_patterns_to_universe(self):
        outomaatti = OutomaattiService(3, 3)
        outomaatti.add_pattern(0, 0, self.blinker_vertical)
        self.assertEqual(outomaatti.get_universe_as_text(), ".*.\n.*.\n.*.\n")
        outomaatti.add_pattern(0, 0, self.blinker_horizontal)
        self.assertEqual(outomaatti.get_universe_as_text(), ".*.\n***\n.*.\n")

    def test_add_patterns_partly_outside_universe(self):
        outomaatti = OutomaattiService(3, 3)
        outomaatti.add_pattern(2, 1, self.blinker_horizontal)
        self.assertEqual(outomaatti.get_universe_as_text(), "...\n...\n..*\n")

    def test_add_patterns_completely_outside_universe(self):
        outomaatti = OutomaattiService(3, 3)
        outomaatti.add_pattern(10, 10, self.blinker_horizontal)
        self.assertEqual(outomaatti.get_universe_as_text(), "...\n...\n...\n")

    def test_simulate_universe(self):
        outomaatti = OutomaattiService(3, 3)
        outomaatti.add_pattern(0, 0, self.blinker_vertical)
        outomaatti.next_generation()
        self.assertEqual(outomaatti.get_universe_as_text(), "...\n***\n...\n")

    def test_count_cells_in_universe(self):
        outomaatti = OutomaattiService(3, 3)
        outomaatti.add_pattern(0, 0, self.blinker_vertical)
        self.assertEqual(outomaatti.count_cells(), 3)

    def test_add_cell_outside_universe(self):
        outomaatti = OutomaattiService(1, 1)
        outomaatti.add_cell(1, 1)
        self.assertEqual(outomaatti.get_universe_as_text(), ".\n")

    def test_clear_universe(self):
        outomaatti = OutomaattiService(1, 1)
        outomaatti.add_cell(0, 0)
        self.assertEqual(outomaatti.get_universe_as_text(), "*\n")
        outomaatti.clear_universe()
        self.assertEqual(outomaatti.get_universe_as_text(), ".\n")

    def test_menu_open_closed_works(self):
        self.assertEqual(self.outomaatti.is_menu_open(), False)
        self.outomaatti.menu_open()
        self.assertEqual(self.outomaatti.is_menu_open(), True)
        self.outomaatti.menu_closed()
        self.assertEqual(self.outomaatti.is_menu_open(), False)

    def test_increasing_size_works(self):
        outomaatti = OutomaattiService(10, 10)
        outomaatti.change_size(1)
        self.assertEqual(outomaatti.get_width(), 20)
        self.assertEqual(outomaatti.get_height(), 20)

    def test_decreasing_size_works(self):
        outomaatti = OutomaattiService(20, 20)
        outomaatti.change_size(-1)
        self.assertEqual(outomaatti.get_width(), 10)
        self.assertEqual(outomaatti.get_height(), 10)

    def test_decreasing_size_under_minimum_does_not_work(self):
        outomaatti = OutomaattiService(11, 11)
        outomaatti.change_size(-1)
        self.assertEqual(outomaatti.get_width(), 11)
        self.assertEqual(outomaatti.get_height(), 11)

    def test_importing_pattern_works(self):
        self.assertEqual(self.outomaatti.import_pattern(
            settings.resources.directory_patterns + "_valid.rle"), "Tiedoston lisäys tietokantaan onnistui!")

    def test_returns_rulesets(self):
        self.assertNotEqual(self.outomaatti.get_rulesets(),
                            len(settings.rules.enabled))

    def test_rulesets_can_be_changed(self):
        if len(settings.rules.enabled) > 1:
            self.assertEqual(self.outomaatti.get_ruleset(), 0)
            self.outomaatti.set_ruleset(1)
            self.assertEqual(self.outomaatti.get_ruleset(), 1)

    def test_returns_running_status(self):
        self.assertEqual(self.outomaatti.is_running(), False)

    def test_can_change_running_status(self):
        self.assertEqual(self.outomaatti.is_running(), False)
        self.outomaatti.pause()
        self.assertEqual(self.outomaatti.is_running(), False)
        self.outomaatti.play()
        self.assertEqual(self.outomaatti.is_running(), True)
        self.outomaatti.pause()
        self.assertEqual(self.outomaatti.is_running(), False)

    def test_returns_speed(self):
        self.assertEqual(self.outomaatti.get_speed(), 1)

    def test_can_change_speed(self):
        self.assertEqual(self.outomaatti.get_speed(), 1)
        self.outomaatti.set_speed(1)
        self.assertEqual(self.outomaatti.get_speed(), 1)
        self.outomaatti.set_speed(3)
        self.assertEqual(self.outomaatti.get_speed(), 3)

    def test_change_speed_to_invalid_value_does_not_work(self):
        self.assertEqual(self.outomaatti.get_speed(), 1)
        self.outomaatti.set_speed(88)
        self.assertEqual(self.outomaatti.get_speed(), 1)

    def test_returns_generation(self):
        self.assertEqual(self.outomaatti.get_generation(), 0)

    def test_generation_increases(self):
        self.assertEqual(self.outomaatti.get_generation(), 0)
        self.outomaatti.next_generation()
        self.assertEqual(self.outomaatti.get_generation(), 1)

    def test_generation_resets(self):
        self.assertEqual(self.outomaatti.get_generation(), 0)
        self.outomaatti.next_generation()
        self.assertEqual(self.outomaatti.get_generation(), 1)
        self.outomaatti.reset_generation()
        self.assertEqual(self.outomaatti.get_generation(), 0)

    def test_forced_redraw_works(self):
        self.assertEqual(self.outomaatti.is_redraw_needed(), True)

    def test_returns_categories(self):
        self.assertEqual(len(self.outomaatti.get_categories()), 11)

    def test_returns_pattern_by_id(self):
        self.assertEqual(self.outomaatti.get_pattern_by_id(3).name, "Syringe")

    def test_returns_pattern_by_name(self):
        self.assertEqual(self.outomaatti.get_pattern_by_name(
            "Syringe").name, "Syringe")

    def test_returns_patterns_by_category(self):
        self.assertEqual(len(self.outomaatti.get_patterns_by_category(10)), 12)

    def test_placing_pattern_in_queue_works(self):
        self.assertEqual(self.outomaatti.get_pattern_queue(), None)
        self.outomaatti.set_pattern_queue(1)
        self.assertEqual(self.outomaatti.get_pattern_queue(), 1)
        self.assertEqual(self.outomaatti.get_pattern_queue(), None)
