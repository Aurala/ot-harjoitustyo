class Pattern:

    def __init__(self, id, category, name, comments, pattern, meta, x_coord, y_coord, rules, hash):
        #self.id = id
        #self.name = name
        #self.category = category
        #self.comments = comments
        self.pattern = pattern
        #self.meta = meta
        #self.x_coord = x_coord
        #self.y_coord = y_coord
        #self.rules = rules
        #self.hash = hash

    def __str__(self):
        return f"Rule {self.id}: {self.name}"
