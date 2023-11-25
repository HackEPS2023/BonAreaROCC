class Tile:
    x = 0
    y = 0
    description = 0
    picking_x = 0
    picking_y = 0


    def __init__(self, x, y, description, picking_x, picking_y):
        self.x = x
        self.y = y
        self.description = description
        self.picking_x = picking_x
        self.picking_y = picking_y
