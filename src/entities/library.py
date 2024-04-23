class Library:

    def __init__(self, patterns, categories, rules):
        self.patterns = patterns
        self.categories = categories
        self.rules = rules

    def get_patterns(self):
        return self.patterns

    def get_categories(self):
        return self.categories

    def get_rules(self):
        return self.rules
