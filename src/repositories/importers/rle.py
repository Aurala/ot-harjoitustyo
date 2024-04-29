import re

# RLE format explained: https://conwaylife.com/wiki/Run_Length_Encoded

# FIX: error handling


class RLE:

    def __init__(self):
        pass

    def parse_metadata(self, content):
        metadata = []
        name = ""
        for line in content:
            line = line.strip()
            if line.startswith("#"):
                metadata.append(line)
            if line.startswith("#N"):
                name = line[2:].strip()
        return (name, "\n".join("".join(row) for row in metadata) + "\n")

    # This function borrows some RLE-parsing code from Justin Reppert's Game of Life
    # project at https://github.com/reppertj/Game-of-Life/blob/master/lifereader.py
    # published under the MIT license.
    # FIX: In some data files birth and survive conditions are in lowercase
    def parse_data(self, content):

        lines = [line for line in content if line.strip()[0] != "#"]
        header = lines[0]
        lines = lines[1:]
        lines = "".join(lines).strip("\n")
        header_pattern = re.compile(
            r"x\s?=\s?(\d+).*?y\s?=\s?(\d+).*?B(\d+).*?S(\d+.)")
        header_matches = header_pattern.search(header)
        width = int(header_matches.group(1))
        height = int(header_matches.group(2))
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

    def read_from_file(self, filename):

        rle_file = open(filename, "r")
        rle_data = rle_file.readlines()

        name, metadata = self.parse_metadata(rle_data)
        rules, pattern = self.parse_data(rle_data)

        return (name, rules, pattern, metadata)
