import pygame as pg

class Screen():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    
    def load_map(self, mapName):
        try:
            with open(mapName, "r") as file:
                level = [list(line.strip()) for line in file.readlines()]
                return level
        except FileNotFoundError:
            print("No level found")
            return 0
    

    def draw_map(self, level, TILE_SIZE, SCREEN):
        for row_x, row in enumerate(level):
            for col_x, tile in enumerate(row):
                if tile == "1":
                    pg.draw.rect(SCREEN, (0, 0, 0), ((col_x * TILE_SIZE, row_x * TILE_SIZE), (TILE_SIZE, TILE_SIZE)))
                if tile == "2":
                    pg.draw.rect(SCREEN, (250, 0, 0), ((col_x * TILE_SIZE, row_x * TILE_SIZE), (TILE_SIZE, TILE_SIZE)))