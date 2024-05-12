class Category:
    """
    Class holds information about one pattern category.

    Attributes match the columns in the database table 'Columns'.

    Attributes:
        category_id (int): Unique identifier.
        name (str): Name.
        description (str): Arbitrary information about the category.
    """

    def __init__(self, category_id, name, description):
        """Class constructor for creating a new Category.

        Args:
            category_id (int): Unique identifier.
            name (str): Category's name.
            description (str): Category's description.
        """
        self._category_id = category_id
        self._name = name
        self._description = description

    @property
    def category_id(self):
        """Returns the category's identifier.

        Returns:
            int: Category's identifier.
        """
        return self._category_id

    @property
    def name(self):
        """Returns the category's name.

        Returns:
            str: Category's name.
        """
        return self._name

    @property
    def description(self):
        """Returns the category's description.

        Returns:
            str: Sategory's description.
        """
        return self._description
