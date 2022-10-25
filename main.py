import pygame
from props import props, Prop
from window import Window
import utils
import sys

window = Window()
window.drawGrid()

players = [
    {
        "inventory": [props[15]]
    },
    {
        "inventory": [props[15]]
    },
    {
        "inventory": [props[15]]
    },
    {
        "inventory": [props[15]]
    }
]
prop = [Prop((100, 200), props[15]), Prop((200, 200), props[5]), Prop((300, 200), props[8])]
group = pygame.sprite.RenderPlain()

selected = False
selection = Prop

for p in prop:
    group.add(p)

while True:
    window.view.blit(window.background, (0, 0))
    window.view.blit(window.grid, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            touch_prop = False
            for p in prop:
                if p.click(event) and not selected:
                    selection = p if not selected else None
                    selection.toggleSelect()
                    selected = not selected
                    touch_prop = True
                    print(selected, selection)

            if selected and not touch_prop:
                grid_pos = utils.convertToGridPos(pygame.mouse.get_pos())
                print("mooving to", grid_pos)
                selection.rect.x, selection.rect.y = grid_pos[0]*25, grid_pos[1]*25
                if True:
                    selection.toggleSelect()
                    selected = False
                    selection = None

    group.draw(window.view)
    pygame.display.flip()
