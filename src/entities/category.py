class Category:
    """
    Class holds information about one category.

    Attributes match the columns in the database table 'Columns'.

    Attributes:
        category_id: integer, Pattern uses this to link to a Category
        name: string, the category's name
        description: string, arbitrary information about the category
    """

    def __init__(self, category_id, name, description):
        """
        Class constructor that creates a new Pattern.

        Args:
            category_id (int): the identifier of the category
            name (str): the category's name
            description (str): arbitrary information about the category
        """
        self._category_id = category_id
        self._name = name
        self._description = description

    @property
    def category_id(self):
        """
        Returns the category's unique id (as set in the database).

        Returns:
            int: Category id (unique)
        """
        return self._category_id

    @property
    def name(self):
        """
        Returns the category's name.

        Returns:
            str: Category's name
        """
        return self._name

    @property
    def description(self):
        """
        Returns the category description.

        Returns:
            str: Category's description
        """
        return self._description
