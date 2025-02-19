import pygame as pg

class World():
    def __init__(self, dirtImg, lavaImg, TILE_SIZE):
        self.dirtImg = pg.image.load(dirtImg)
        self.dirtImg = pg.transform.scale(self.dirtImg, (TILE_SIZE, TILE_SIZE))
        self.lavaImg = pg.image.load(lavaImg)
        self.lavaImg = pg.transform.scale(self.lavaImg, (TILE_SIZE, TILE_SIZE))

        self.tileList = []
        self.TILE_SIZE = TILE_SIZE


    def load_map(self, mapName):
        try:
            with open(mapName, "r") as file:
                level = [list(line.strip()) for line in file.readlines()]
                return level
        except FileNotFoundError:
            print("No level found")
            return 0
    

    def draw_map(self, SCREEN):
        for tile in self.tileList:
            SCREEN.blit(tile[0], tile[1])
    

    def load_tiles(self, level):
        self.tileList = []
        for row_index, row in enumerate(level):
            for col_index, tile in enumerate(row):
                if tile == "1" or tile == "2":
                    img = pg.transform.scale(self.dirtImg if tile == "1" else self.lavaImg, (self.TILE_SIZE, self.TILE_SIZE))
                    imgRect = pg.Rect(col_index * self.TILE_SIZE, row_index * self.TILE_SIZE, self.TILE_SIZE, self.TILE_SIZE)
                    tile = (img, imgRect)
                    self.tileList.append(tile)