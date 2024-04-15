class Pattern:

    def __init__(self, pattern_id, category_id, name, rules_id, pattern, metadata):
        self.pattern_id = pattern_id
        self.category_id = category_id
        self.name = name
        self.rules_id = rules_id
        self.pattern = pattern
        self.metadata = metadata

    def __str__(self):
        return f"Rule {self.pattern_id}: {self.name}"
