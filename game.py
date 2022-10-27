import pygame
import utils
from player import Player
from props import PROPS, Prop
from grid import Grid

RED = (255, 10, 10)
GREEN = (10, 255, 10)
BLUE = (10, 10, 255)
YELLOW = (255, 255, 10)

class Game:

    def __init__(self, grid):
        self.player = 0
        self.players = [Player(RED), Player(GREEN), Player(BLUE), Player(YELLOW)]
        self.grid = grid
        self.selection = None
        self.props = pygame.sprite.RenderPlain()
        self.updateDisplayedProps()

    def nextPlayer(self):
        self.player = (self.player + 1) % 4
        print("Player :", self.player + 1)
        self.updateDisplayedProps()

    def updateDisplayedProps(self):
        self.props.empty()
        for p in self.getCurrentPlayer().inventory: self.props.add(p)

    def handleKeyDown(self, event):
        if event.key == pygame.K_r:
            if self.selection: self.selection.rotate()

    def handleMouseDown(self, event):
        touch_prop = False
        for p in self.getCurrentPlayer().inventory:
            if p.click(event) and not self.selection and not p.placed:
                self.selection = p if not self.selection else None
                self.selection.toggleSelect()
                touch_prop = True

        if self.selection and not touch_prop:
            grid_pos = utils.convertToGridPos(pygame.mouse.get_pos())

            if not self.grid.isPropFitting(self.selection, grid_pos):
                print("Can't fit in grid")
                return
            if self.grid.isPropOverlapping(self.selection, grid_pos):
                print("Overlapping")
                return

            if self.getCurrentPlayer().first_move:
                # WRONG PLACEMENT
                if not self.grid.isValidFirstMove(self.selection, grid_pos, self.player):
                    print("Invalid first move")
                    return
                # FIRST MOVE SUCCEED
                self.getCurrentPlayer().first_move = False

            self.selection.rect.x, self.selection.rect.y = grid_pos[0] * 25, grid_pos[1] * 25
            self.grid.placeProp(self.selection, grid_pos, self.player)

            self.grid.props["list"].append(self.selection)
            self.grid.props["group"].add(self.selection)

            self.selection.toggleSelect()
            self.selection.placed = True
            self.selection = None
            self.nextPlayer()

    def getCurrentPlayer(self):
        return self.players[self.player]
