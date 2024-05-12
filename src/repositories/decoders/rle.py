import re
from datetime import datetime


class RLE:
    """
    Class provides a set of methods to decode patterns that are stored in the
    Run Length Encoded (RLE) format.

    Explanation of the format: https://conwaylife.com/wiki/Run_Length_Encoded

    RLE files one can found online have small deviations and this decoder is
    not able to parse all of them.
    """

    def __init__(self):
        """
        Class constructor. Takes no arguments.
        """

    def parse_metadata(self, content):
        """
        Parses metadata (all lines starting with a hash) from a string containing
        a Run Length Encoded pattern.

        The pattern's name is extracted from metadata.

        Args:
            content (str): the RLE data

        Returns:
            (str, str): the pattern's name, the rest of the metadata
        """

        metadata = []
        name = "Tuntematon " + str(datetime.now())
        for line in content:
            line = line.strip()
            if line.startswith("#"):
                metadata.append(line)
            if line.startswith("#N"):
                name = line[2:].strip()
        return (name, "\n".join("".join(row) for row in metadata) + "\n")

    def parse_data(self, content):
        """
        Parses pattern data (all lines not starting with a hash) from a string
        containing a Run Length Encoded pattern.

        The function borrows some regexp magic from Justin Reppert's
        Game of Life project published under the MIT license.
        https://github.com/reppertj/Game-of-Life/blob/master/lifereader.py

        Args:
            content (str): the RLE data

        Returns:
            (str, list): the rules the pattern was designed for, the pattern data
        """

        lines = [line for line in content if line.strip()[0] != "#"]
        header = lines[0]
        lines = lines[1:]
        lines = "".join(lines).strip("\n")
        header_pattern = re.compile(
            r"x\s?=\s?(\d+).*?y\s?=\s?(\d+).*?[bB](\d+).*?[sS](\d+.)")
        header_matches = header_pattern.search(header)
        width = int(header_matches.group(1))
        _ = int(header_matches.group(2))
        birth_conditions = header_matches.group(3)
        survive_conditions = header_matches.group(4)
        line_pattern = re.compile(r"(\d*)([bo$!])")
        line_data = line_pattern.findall(lines)
        line_data = [(1, match[1]) if match[0] == "" else (
            int(match[0]), match[1]) for match in line_data]

        pattern = []
        pattern_row = []

        while len(line_data) > 0:
            sequence = line_data[0]
            if sequence[1] == "$" or sequence[1] == "!":
                pattern_row += [0 for _ in range(width-len(pattern_row))]
                pattern.append(pattern_row)
                pattern_row = []
            elif sequence[1] == "b":
                pattern_row += [0 for _ in range(sequence[0])]
            elif sequence[1] == "o":
                pattern_row += [1 for _ in range(sequence[0])]
            line_data = line_data[1:]

        return (f"B{birth_conditions}/S{survive_conditions}", pattern)

    def decode(self, encoded_data):
        """
        Reads Run Length Encoded data from a file and parses it
        for metadata and pattern data.

        Args:
            filename (str): the file that contains the data

        Returns:
            (str, str, list, str):
            the pattern name,
            the rules the pattern wa designed for,
            the pattern data,
            the metadata
        """

        name, metadata = self.parse_metadata(encoded_data)
        rules, pattern = self.parse_data(encoded_data)

        return (name, rules, pattern, metadata)
