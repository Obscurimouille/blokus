from enum import Enum
import pygame
from props import RED, GREEN, BLUE, YELLOW

EMPTY = 0
X = 0
Y = 1

SIZE = 16


class Grid:

    def __init__(self):
        self.grid = [[EMPTY for i in range(SIZE)] for i in range(SIZE)]
        self.props = {
            "list": [],
            "group": pygame.sprite.RenderPlain()
        }
        self.hints = {
            "list": [],
            "group": pygame.sprite.Group()
        }

        self.initHints()

    def initHints(self):
        self.hints["list"] = [Hint(RED, 5, 5), Hint(YELLOW, 5, 5+(SIZE-1)*25), Hint(BLUE, 5+(SIZE-1)*25, 5+(SIZE-1)*25), Hint(GREEN, 5+(SIZE-1)*25, 5)]
        for hint in self.hints["list"]:
            self.hints["group"].add(hint)

    def print(self):
        print("---------------------------------------")
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                print(self.grid[i][j], ", ", end="", sep="")
            print()

    def isValidFirstMove(self, prop, pos, player):
        if player == 0:
            return pos[0] == 0 and pos[1] == 0 and prop.pattern[0][0]
        elif player == 1:
            return pos[0]+len(prop.pattern[0]) == SIZE and pos[1] == 0 and prop.pattern[0][-1]
        elif player == 2:
            return pos[0]+len(prop.pattern[0]) == SIZE and (pos[1]+len(prop.pattern) == SIZE and prop.pattern[-1][-1])
        elif player == 3:
            return pos[0] == 0 and pos[1]+len(prop.pattern) == SIZE and prop.pattern[-1][0]

    def isPropFittingInGrid(self, prop, pos):
        # VALID X
        if len(prop.pattern[0]) > SIZE - pos[0]: return False
        # VALID Y
        if len(prop.pattern) > SIZE - pos[1]: return False
        return True

    def isTileValid(self, pos, player):
        deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for delta in deltas:
            # CLAMP X & Y TO GRID
            x, y = max(min(pos[0] + delta[X], SIZE - 1), 0), max(min(pos[1] + delta[Y], SIZE - 1), 0)
            if self.grid[y][x] == player+1: return False

        return True

    def isTileTouchCorner(self, pos, player):
        deltas = [(-1, 1), (1, 1), (1, -1), (-1, -1)]

        for delta in deltas:
            # CLAMP X & Y TO GRID
            x, y = max(min(pos[0] + delta[X], SIZE - 1), 0), max(min(pos[1] + delta[Y], SIZE - 1), 0)
            if self.grid[y][x] == player+1: return True

        return False

    def placeProp(self, prop, pos, player):
        for dy in range(len(prop.pattern)):
            for dx in range(len(prop.pattern[dy])):
                if prop.pattern[dy][dx]: self.grid[pos[1]+dy][pos[0]+dx] = player + 1

    def isValidMove(self, prop, pos, player, first_move):
        is_placed_on_corner = False
        for dy in range(len(prop.pattern)):
            for dx in range(len(prop.pattern[dy])):
                # CLAMP X & Y TO GRID
                x, y = max(min(pos[0]+dx, SIZE-1), 0), max(min(pos[1]+dy, SIZE-1), 0)
                if prop.pattern[dy][dx]:
                    if self.grid[y][x] != EMPTY or not self.isTileValid((x, y), player): return False
                    if not first_move and not is_placed_on_corner and self.isTileTouchCorner((x, y), player): is_placed_on_corner = True

        return is_placed_on_corner or first_move

    def isAnyValidMove(self, player, first_move,nb_player):
        if first_move: return True
        inv = player.inventory.copy()

        self.print()
        for prop in inv:
            for posy in range(len(self.grid)):
                for posx in range(len(self.grid[posy])):
                    pos = (posx,posy)
                    rf = 0
                    while rf <= 8:
                        if rf in [1, 2, 3, 5, 6, 7, 8]:
                            prop.rotate()
                        if rf == 4:
                            prop.rotate()
                            prop.flip()
                        if self.isPropFittingInGrid(prop, pos) and self.isValidMove(prop, pos, nb_player, first_move):
                            print("tu peux encore jouer {}".format(player.color))
                            return True
                        rf += 1
        print("tu ne peux plus jouer {}".format(player.color))
        return False


class Hint(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()

        self.image = pygame.Surface([16, 16])
        self.image.fill(pygame.SRCALPHA)

        pygame.draw.circle(self.image, color, (8, 8), 5)

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
