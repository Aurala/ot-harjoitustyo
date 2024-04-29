class Pattern:

    def __init__(self, pattern_id, category_id, name, rules, pattern, metadata):
        self._pattern_id = pattern_id
        self._category_id = category_id
        self._rules = rules
        self._name = name
        self._pattern = pattern
        self._metadata = metadata

    @property
    def pattern_id(self):
        return self._pattern_id

    @property
    def category_id(self):
        return self._category_id

    @property
    def name(self):
        return self._name

    @property
    def rules(self):
        return self._rules

    @property
    def pattern(self):
        return self._pattern

    @property
    def metadata(self):
        return self._metadata

    def __str__(self):
        return f"Pattern {self._pattern_id}: {self._name}"
