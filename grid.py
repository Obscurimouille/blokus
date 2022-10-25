from enum import Enum

class Tile(Enum):
    EMPTY = 0
    USED = 1

SIZE = 20

class Grid:

    def __init__(self):
        self.grid = [[Tile.EMPTY for i in range(SIZE)] for i in range(SIZE)]
        print(self.grid)

    def isPropFitting(self, prop, pos):
        # VALID X
        if len(prop.pattern[0]) > SIZE - pos[0]: return False
        # VALID Y
        if len(prop.pattern) > SIZE - pos[1]: return False
        return True