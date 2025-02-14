import pygame as pg

class World():
    def __init__(self, dirtImg, lavaImg, TILE_SIZE):
        self.dirtImg = pg.image.load(dirtImg)
        self.dirtImg = pg.transform.scale(self.dirtImg, (TILE_SIZE, TILE_SIZE))
        self.lavaImg = pg.image.load(lavaImg)
        self.lavaImg = pg.transform.scale(self.lavaImg, (TILE_SIZE, TILE_SIZE))

        self.tileList = []


    def load_map(self, mapName):
        try:
            with open(mapName, "r") as file:
                level = [list(line.strip()) for line in file.readlines()]
                return level
        except FileNotFoundError:
            print("No level found")
            return 0
    

    def draw_map(self, level, TILE_SIZE, SCREEN):
        for x, row in enumerate(level):
            for y, tile in enumerate(row):
                if tile == "1":
                    SCREEN.blit(self.dirtImg, (y * TILE_SIZE, x * TILE_SIZE))
                if tile == "2":
                    SCREEN.blit(self.lavaImg, (y * TILE_SIZE, x * TILE_SIZE))
    

    def load_tiles(self, level, TILE_SIZE):
        for x, row in enumerate(level):
            for y, tile in enumerate(row):
                if tile == "1":
                    img = pg.transform.scale(self.dirtImg, (TILE_SIZE, TILE_SIZE))
                    imgRect = img.get_rect()
                    imgRect.x = x * TILE_SIZE
                    imgRect.y = y * TILE_SIZE
                    tile = (img, imgRect)
                    print(tile[1])
                    self.tileList.append(tile)
                if tile == "2":
                    img = pg.transform.scale(self.lavaImg, (TILE_SIZE, TILE_SIZE))
                    imgRect = img.get_rect()
                    imgRect.x = x * TILE_SIZE
                    imgRect.y = y * TILE_SIZE
                    tile = (img, imgRect)
                    self.tileList.append(tile)

