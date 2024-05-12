class Pattern:
    """Class holding information about one pattern.

    Attributes match the columns in the database table 'Patterns'.

    Attributes:
        pattern_id (int): Unique identifier.
        category_id (int): Links the pattern to a category.
        name (str): Pattern's name.
        rules (str): Rules this pattern was designed for.
        pattern (list): Pattern data.
        metadata (str): Arbitrary information about the pattern.
    """

    def __init__(self, pattern_id, category_id, name, rules, pattern, metadata):
        """Class constructor for creating a new Pattern.

        Args:
            pattern_id (int): Unique identifier.
            category_id (int): Links the pattern to a category.
            name (str): Pattern's name
            rules (str): Rules this pattern was designed for.
            pattern (list): Pattern's data.
            metadata (st): Arbitrary information about the pattern.
        """
        self._pattern_id = pattern_id
        self._category_id = category_id
        self._name = name
        self._rules = rules
        self._pattern = pattern
        self._metadata = metadata

    @property
    def pattern_id(self):
        """Returns the pattern's identifier.

        Returns:
            int: Pattern's identifier.
        """
        return self._pattern_id

    @property
    def category_id(self):
        """Returns the category this pattern belongs to.

        Returns:
            int: Category's identifier.
        """
        return self._category_id

    @property
    def name(self):
        """
        Returns the pattern's name.

        Returns:
            str: Pattern's name.
        """
        return self._name

    @property
    def rules(self):
        """Returns the ideal rules the pattern was designed for.

        Patterns can be used with any rules. This information
        exists only because some patterns do not do anything
        interesting with "wrong" rules.

        Returns:
            str: Rules the pattern was designed for.
        """
        return self._rules

    @property
    def pattern(self):
        """Returns the pattern data.

        Returns:
            list: 2D array containing the pattern data.
        """
        return self._pattern

    @property
    def metadata(self):
        """Returns the pattern metadata.

        Metadata means all comments included in the imported file:
        - name
        - creator
        - description + any other arbitrary data in the imported file

        Returns:
            str: Pattern's metadata.
        """
        return self._metadata
