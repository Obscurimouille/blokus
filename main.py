import pygame
from grid import Grid
from props import PROPS, Prop
from window import Window
import sys
from game import Game

grid = Grid()
game = Game(grid)
window = Window()
window.drawGrid(grid.grid)

while True:
    window.view.blit(window.background, (0, 0))
    window.view.blit(window.grid, (0, 0))

    for event in pygame.event.get():
        # EXIT GAME
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # MOUSEDOWN
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            game.handleMouseDown(event)
            # grid.print()
        if event.type == pygame.KEYDOWN:
            game.handleKeyDown(event)

    game.props.draw(window.view)
    game.grid.props["group"].draw(window.view)
    pygame.display.flip()
