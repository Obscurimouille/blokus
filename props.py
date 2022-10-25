import pygame

RED = (255, 10, 10)
RED_LIGHT = (255, 80, 72)

props = [
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

    def __init__(self, pos, prop):
        super().__init__()
        self.size = 25
        self.locked = False
        self.selected = False
        self.length = prop["length"]
        self.pattern = prop["pattern"]

        self.image = pygame.Surface((100, 100), pygame.SRCALPHA, 32)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

        self.draw()

        # Create the collision mask (anything not transparent)
        self.mask = pygame.mask.from_surface(self.image)

    def toggleSelect(self):
        self.selected = not self.selected
        self.draw()

    def draw(self):
        for i in range(len(self.pattern)):
            for j in range(len(self.pattern[i])):
                if self.pattern[i][j]:
                    pygame.draw.rect(self.image, RED_LIGHT if self.selected else RED, pygame.Rect((j*self.size, i*self.size), (self.size, self.size)))

    def click(self, event):
        mouse_pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            collid = self.rect.collidepoint(mouse_pos)
            return collid

