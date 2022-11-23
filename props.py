import pygame

ANGLE_0 = 0
ANGLE_90 = 1
ANGLE_180 = 2
ANGLE_170 = 3

RED = (255, 10, 10)
GREEN = (10, 255, 10)
BLUE = (10, 10, 255)
YELLOW = (255, 255, 10)

PROPS = [
    # PIECES DE 1
    {
        "length": 1,
        "pattern": [
            [1]
        ]
    },
    # PIECES DE 2
    {
        "length": 2,
        "pattern": [
            [1, 1]
        ]
    },
    # PIECES DE 3
    {
        "length": 3,
        "pattern": [
            [1, 1, 1]
        ]
    },
    {
        "length": 3,
        "pattern": [
            [1, 1],
            [1, 0]
        ]
    },
    # PIECES DE 4
    {
        "length": 4,
        "pattern": [
            [1, 1, 1, 1]
        ]
    },
    {
        "length": 4,
        "pattern": [
            [1, 1, 1],
            [1, 0, 0]
        ]
    },
    {
        "length": 4,
        "pattern": [
            [1, 1, 1],
            [0, 1, 0]
        ]
    },
    {
        "length": 4,
        "pattern": [
            [1, 1],
            [1, 1]
        ]
    },
    {
        "length": 4,
        "pattern": [
            [1, 1, 0],
            [0, 1, 1]
        ]
    },
    # PIECES DE 5
    {
        "length": 5,
        "pattern": [
            [1, 1, 1, 1, 1]
        ]
    },
    {
        "length": 5,
        "pattern": [
            [1, 1, 1, 1],
            [1, 0, 0, 0]
        ]
    },
    {
        "length": 5,
        "pattern": [
            [1, 1, 1, 0],
            [0, 0, 1, 1]
        ]
    },
    {
        "length": 5,
        "pattern": [
            [1, 1, 1, 1],
            [0, 1, 0, 0]
        ]
    },
    {
        "length": 5,
        "pattern": [
            [1, 1, 1],
            [1, 1, 0]
        ]
    },
    {
        "length": 5,
        "pattern": [
            [1, 1, 1],
            [1, 0, 1]
        ]
    },
    {
        "length": 5,
        "pattern": [
            [1, 1, 1],
            [0, 1, 0],
            [0, 1, 0]
        ]
    },
    {
        "length": 5,
        "pattern": [
            [1, 1, 1],
            [1, 0, 0],
            [1, 0, 0]
        ]
    },
    {
        "length": 5,
        "pattern": [
            [0, 1, 1],
            [1, 1, 0],
            [1, 0, 0]
        ]
    },
    {
        "length": 5,
        "pattern": [
            [1, 0, 0],
            [1, 1, 1],
            [0, 0, 1]
        ]
    },
    {
        "length": 5,
        "pattern": [
            [1, 0, 0],
            [1, 1, 1],
            [0, 1, 0]
        ]
    },
    {
        "length": 5,
        "pattern": [
            [0, 1, 0],
            [1, 1, 1],
            [0, 1, 0]
        ]
    }
]

class Prop(pygame.sprite.Sprite):

    def __init__(self, pos, prop, color=(128, 128, 128)):
        super().__init__()
        self.rotation = ANGLE_0
        self.size = 25
        self.color = color
        self.highlight_color = self.getHighlight(color)
        self.placed = False
        self.selected = False
        self.length = prop["length"]
        self.pattern = prop["pattern"]

        self.image = pygame.Surface((self.length*self.size, self.length*self.size), pygame.SRCALPHA, 32)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

        self.draw()

        # Create the collision mask (anything not transparent)
        self.mask = pygame.mask.from_surface(self.image)

    def toggleSelect(self):
        self.selected = not self.selected
        self.draw()

    def flip(self):
        self.erase()
        # https://stackoverflow.com/questions/53250821/in-python-how-do-i-rotate-a-matrix-90-degrees-counterclockwise
        self.pattern = self.pattern[::-1]
        self.draw()

    def rotate(self):
        self.erase()
        # https://stackoverflow.com/questions/53250821/in-python-how-do-i-rotate-a-matrix-90-degrees-counterclockwise
        self.pattern = [[self.pattern[j][i] for j in range(len(self.pattern))] for i in range(len(self.pattern[0])-1, -1, -1)]
        self.draw()

    def print(self):
        print("---------")
        for i in range(len(self.pattern)):
            for j in range(len(self.pattern[i])):
                print(self.pattern[i][j], ", ", end="", sep="")
            print()
        print("---------")

    def erase(self):
        for i in range(len(self.pattern)):
            for j in range(len(self.pattern[i])):
                if self.pattern[i][j]:
                    pygame.draw.rect(self.image, pygame.SRCALPHA, pygame.Rect((j*self.size, i*self.size), (self.size, self.size)))

    def draw(self):
        for i in range(len(self.pattern)):
            for j in range(len(self.pattern[i])):
                if self.pattern[i][j]:
                    pygame.draw.rect(self.image, self.highlight_color if self.selected else self.color, pygame.Rect((j*self.size, i*self.size), (self.size, self.size)))

    def click(self, event):
        mouse_pos = pygame.mouse.get_pos()
        print(mouse_pos)
        print(self.image.get_rect().topleft)
        if pygame.mouse.get_pressed()[0]:
            return self.rect.collidepoint(mouse_pos)

    def getHighlight(self, color, gain=10):
        r, g, b = color
        return int(r + gain * r * (1 - (r / 255))), int(g + gain * g * (1 - (g / 255))), int(b + gain * b * (1 - (b / 255)))
