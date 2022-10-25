import pygame
import utils
from props import PROPS, Prop
from grid import Grid

class Game:

    def __init__(self, grid):
        self.grid = grid
        self.selected = False
        self.selection = Prop
        self.props = [Prop((100, 200), PROPS[15]), Prop((200, 200), PROPS[5]), Prop((300, 200), PROPS[8])]

    def handleMouseDown(self, event):
        touch_prop = False
        for p in self.props:
            if p.click(event) and not self.selected:
                self.selection = p if not self.selected else None
                self.selection.toggleSelect()
                self.selected = not self.selected
                touch_prop = True
                print(self.selected, self.selection)

        if self.selected and not touch_prop:
            grid_pos = utils.convertToGridPos(pygame.mouse.get_pos())
            if not self.grid.isPropFitting(self.selection, grid_pos):
                print("Can't fit in grid")
            else:
                self.selection.rect.x, self.selection.rect.y = grid_pos[0] * 25, grid_pos[1] * 25
                if True:
                    self.selection.toggleSelect()
                    self.selected = False
                    self.selection = None