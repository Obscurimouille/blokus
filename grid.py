from enum import Enum
import pygame

EMPTY = 0
USED = 1

SIZE = 16

class Grid:

    def __init__(self):
        self.grid = [[EMPTY for i in range(SIZE)] for i in range(SIZE)]
        self.props = {
            "list": [],
            "group": pygame.sprite.RenderPlain()
        }
        print(self.grid)

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
            return (pos[0]+len(prop.pattern[0]) == SIZE and prop.pattern[0][-1]) and (pos[1]+len(prop.pattern) == SIZE and prop.pattern[-1][-1])
        elif player == 3:
            return pos[0] == 0 and pos[1]+len(prop.pattern) == SIZE and prop.pattern[-1][0]

    def isPropFitting(self, prop, pos):
        # VALID X
        if len(prop.pattern[0]) > SIZE - pos[0]: return False
        # VALID Y
        if len(prop.pattern) > SIZE - pos[1]: return False
        return True

    def placeProp(self, prop, pos, player):
        for dy in range(len(prop.pattern)):
            for dx in range(len(prop.pattern[dy])):
                if prop.pattern[dy][dx]: self.grid[pos[1]+dy][pos[0]+dx] = player + 1

    def isPropOverlapping(self, prop, pos):
        for dy in range(len(prop.pattern)):
            for dx in range(len(prop.pattern[dy])):
                x, y = pos[0]+dx, pos[1]+dy
                if x > SIZE-1: x = SIZE-1
                if y > SIZE-1: y = SIZE-1
                print(x, y, dx, dy)

                if prop.pattern[dy][dx] and self.grid[y][x]: return True
        return False