import pygame

screen_width = 800
screen_height = 800

WHITE = (255, 255, 255)
BLACK = (10, 10, 10)
GRAY = (90, 90, 90)

class Window:

    def __init__(self):
        pygame.init()

        # WINDOW
        pygame.display.set_caption("Blokus")
        self.view = pygame.display.set_mode((screen_width, screen_height))
        self.view.fill((250, 250, 255))
        self.background = pygame.Surface((screen_width, screen_height))
        self.grid = pygame.Surface((screen_width, screen_height))

        clock = pygame.time.Clock()

    def drawGrid(self, size=20):
        blockSize = 25 # Set the size of the grid block
        for x in range(size):
            for y in range(size):
                rect = pygame.Rect(x*blockSize, y*blockSize, blockSize, blockSize)
                pygame.draw.rect(self.grid, GRAY, rect, 2)
