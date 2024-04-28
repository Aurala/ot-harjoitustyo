class Category:

    def __init__(self, category_id, name, description):
        self._category_id = category_id
        self._name = name
        self._description = description

    @property
    def category_id(self):
        return self._category_id

    @property
    def name(self):
        return self._name
    
    @property
    def description(self):
        return self._description

    def __str__(self):
        return f"Category {self.category_id}: {self.name}"
