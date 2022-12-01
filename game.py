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
        elif event.key == pygame.K_f:
            if self.selection: self.selection.flip()

    def handleMouseDown(self, event):
        touched_prop = None

        for p in self.getCurrentPlayer().inventory:
            if p.click(event) and not p.placed:
                touched_prop = p
                break

        if touched_prop:
            if touched_prop == self.selection:
                self.selection.toggleSelect()
                self.selection = None
                return

            elif self.selection: self.selection.toggleSelect()

            self.selection = touched_prop
            self.selection.toggleSelect()

        if self.selection and not touched_prop:
            grid_pos = utils.convertToGridPos(pygame.mouse.get_pos())

            if not self.grid.isPropFittingInGrid(self.selection, grid_pos):
                print("Can't fit in grid")
                return
            if not self.grid.isValidMove(self.selection, grid_pos, self.player, self.getCurrentPlayer().first_move):
                print("Wrong placement")
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
            self.getCurrentPlayer().inventory.remove(self.selection)
            self.grid.isAnyValidMove(self.getCurrentPlayer(), self.getCurrentPlayer().first_move,self.player)
            self.selection = None
            self.nextPlayer()

    def getCurrentPlayer(self):
        return self.players[self.player]

    def dispEndGame(self, view):
        font = pygame.font.Font('freesansbold.ttf', 48)

        text = font.render("Félicitations !", True, (255, 255, 255))
        rect = text.get_rect()
        rect.center = (400, 200)

        view.blit(text, rect)

        font = pygame.font.Font('freesansbold.ttf', 32)

        text = font.render("Classement", True, (255, 255, 255))
        rect = text.get_rect()
        rect.center = (400, 325)

        view.blit(text, rect)

        stats = [{"player": 1, "points": 45}, {"player": 2, "points": 12}, {"player": 3, "points": 98}, {"player": 4, "points": 85}]
        self.dispLeaderboard(stats, view, 500)

    def dispLeaderboard(self, stats, view, y = 400):
        stats = sorted(stats, key=lambda d: d['points'])
        line_height = 50
        font = pygame.font.Font('freesansbold.ttf', 24)

        for player, data in enumerate(stats):
            stat = str(player+1) + ". Joueur " + str(data["player"]) + ": " + str(data["points"])
            text = font.render(stat, True, (255, 255, 255))
            rect = text.get_rect()
            rect.center = (400, y - 2*line_height + player * line_height)
            view.blit(text, rect)


