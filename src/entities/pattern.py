class Pattern:
    """
    Class holds information about one pattern.

    Attributes match the columns in the database table 'Patterns'.

    Attributes:
        pattern_id: integer, used to query the pattern from the database
        category_id: integer, links the pattern to a category
        name: string, the pattern's name
        rules: string, the rules the pattern was designed for
        pattern: list, the represented as a 2D array
        metadata: string, arbitrary information about the pattern
    """

    def __init__(self, pattern_id, category_id, name, rules, pattern, metadata):
        """
        Class constructor that creates a new Pattern.

        Args:
            pattern_id (int): the identifier of the pattern
            category_id (int): the identifier of the pattern's category
            name (str): the name of the pattern
            rules (string): the rules this pattern was designed for
            pattern (list): the pattern data
            metadata (string): arbitrary information about the pattern
        """
        self._pattern_id = pattern_id
        self._category_id = category_id
        self._rules = rules
        self._name = name
        self._pattern = pattern
        self._metadata = metadata

    @property
    def pattern_id(self):
        """
        Returns the pattern's unique identifier (as set in the database).

        Returns:
            int: Pattern id (unique)
        """
        return self._pattern_id

    @property
    def category_id(self):
        """
        Returns the unique identifier (as set in the database) of the
        category this pattern belongs to.

        Returns:
            int: Category id (unique)
        """
        return self._category_id

    @property
    def name(self):
        """
        Returns the pattern's name.

        Returns:
            str: Pattern's name
        """
        return self._name

    @property
    def rules(self):
        """
        Returns the ideal rules the pattern was designed for.

        Rules do not restrict the use of pattern with any rules.
        This information exists only because some patterns do not
        do anything interesting with non-ideal rules.

        Returns:
            str: Rules the pattern was designed for
        """
        return self._rules

    @property
    def pattern(self):
        """
        Returns the pattern data.

        Returns:
            list: 2D array containing the pattern
        """
        return self._pattern

    @property
    def metadata(self):
        """
        Returns the pattern metadata.

        Metadata means all comments included in the imported file:
        - name
        - creator
        - description + any other arbitrary comments in the file

        Returns:
            str: _description_
        """
        return self._metadata
