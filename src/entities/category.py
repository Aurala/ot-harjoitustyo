class Category:

    def __init__(self, category_id, name, description):
        self.category_id = category_id
        self.name = name
        self.description = description

    def __str__(self):
        return f"Category {self.category_id}: {self.name}"
