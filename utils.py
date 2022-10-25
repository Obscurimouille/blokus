def convertToGridPos(pos):
    gridSize = 25
    return int(pos[0] / gridSize), int(pos[1] / gridSize)
