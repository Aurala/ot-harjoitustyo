import re

class PatternRepository:

    def __init__(self):
        pass

    def list_patterns(self, category=None):
        pass

    def load_pattern(self):
        pass

    def save_pattern(self):
        pass

    # Adapted from https://github.com/reppertj/Game-of-Life/blob/master/lifereader.py (MIT license)
    # FIX: exception handling
    def parse_rle(self):
        lines = [
            "#C Double p46 gun found by Dieter Leithner pulls blocks and beehives\n",
            "#C Dean Hickerson, 2/21/97; from Jason Summers' 'jslife' collection\n",
            "x = 90, y = 97, rule = B3/S23\n",
            "boo23boo$boo23bo$24bobo$6bo3boo12boo36boo5boo$oobboobob3o50boo5boo$oo\n",
            "bbo4b3o$4bo3bo$5b3o$44boo$5b3o36boo$4bo3bo$oobbo4b3o25boo$oobboobob3o\n",
            "25bobo5boo$6bo3boo25boboo4boo$21boo15boo$boo35bo$boo20bo$23bobo12bo23b\n",
            "oo5boo$20bo17boo21bobbo3bobbo$20bo5bo10boboo4boo17booboo$20bo5bo10bobo\n",
            "5boo16bobobobo$22bo3bo10boo24bobobobo$22bo38bo9bo$22bobbo18boo14bo11bo\n",
            "$22b3o19boo$65bobo$62bo9bo$62bo3bo5boo$32bo31b3o6bo$28boobbo34booboo$\n",
            "27bo5bo13boo$26boobbobo14boo$27boo3bo$28b3o34bo7bo$41boo3boo18bobobobo\n",
            "$28b3o9bobbobobbo17bobobobo$27boo3bo6bo9bo15bobooboobo$26boobbobo5boo\n",
            "9boo14boo5boo$27bo5bo5bo9bo5bo$16boo10boobbo7bobbobobbo5bo$15bobo14bo\n",
            "8boo3boo6b3o$15bo$14boo$$28bo5bo22boo$26bobo3bobo21b4o$27boo4boo20bobb\n",
            "obo$54bobobboo$53bobo$52boo$43bo8b3o10boo5boo$43bobo7bobo9boo5boo$43b\n",
            "oo9boo$$63boo$39bo5bo16b4o7boo$40bo5bo14bobobo6bobboo11boo$38b3o3b3o7b\n",
            "oo5boob3o4b6o11boo$54boo8boobo5b4o$64boobo$$64boobo$64boobo5b4o$30boo\n",
            "31bobbo4b6o11boo$29bobo32boo6bobboo11boo$29bo34boo7boo$28boo9boo$40bo\n",
            "10bo5bo$37b3o9bobo3bobo$37bo12boo4boo$62bo$61bobo$61bobo$62bo5$64boo$\n",
            "64boo$$67boo4bo$67boo3bobo$72bobo$73bo5$75boo$75boo$$78boo$78boo$$81b\n",
            "oo$81boo!\n"]
        
        lines = [line for line in lines if line.strip()[0] != '#']
        header = lines[0]
        lines = lines[1:]
        lines = ''.join(lines).strip('\n')
        header_pattern = re.compile(r'x\s?=\s?(\d+).*?y\s?=\s?(\d+).*?B(\d+).*?S(\d+.)')
        header_matches = header_pattern.search(header)
        #try:
        born = header_matches.group(3)
        survive = header_matches.group(4)
        #except IndexError:
        #    print("No or improper rule in file; defaulting to B3/S23.")
        #    born = "3"
        #    survive = "23"
        width = int(header_matches.group(1))
        height = int(header_matches.group(2))
        line_pattern = re.compile(r'(\d*)([bo$!])')
        line_data = line_pattern.findall(lines)
        line_data = [(1, match[1]) if match[0] == '' else (int(match[0]), match[1]) for match in line_data]
        print(height, width, born, survive, line_data)

if __name__ == "__main__":
    pr = PatternRepository()
    pr.parse_rle()
