import pygame as pg

class World():
    def __init__(self, dirtImg, lavaImg, diamondImg, TILE_SIZE):
        self.dirtImgS = dirtImg
        self.dirtImg = pg.transform.scale(pg.image.load(dirtImg), (TILE_SIZE, TILE_SIZE))
        self.lavaImgS = lavaImg
        self.lavaImg = pg.transform.scale(pg.image.load(lavaImg), (TILE_SIZE, TILE_SIZE))
        self.diamondImgS = diamondImg
        self.diamondImg = pg.transform.scale(pg.image.load(diamondImg), (TILE_SIZE, TILE_SIZE))

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
    
    def get_image(self, tile, source):
        if source:
            if tile == "1":
                return self.dirtImgS
            elif tile == "2":
                return self.lavaImgS
            elif tile == "3":
                return self.diamondImgS
        else:
            if tile == "1":
                return self.dirtImg
            elif tile == "2":
                return self.lavaImg
            elif tile == "3":
                return self.diamondImg
            else:
                return self.dirtImg
    

    def load_tiles(self, level):
        self.tileList = []
        for row_index, row in enumerate(level):
            for col_index, tile in enumerate(row):
                if tile == "1" or tile == "2" or tile == "3":
                    image = self.get_image(tile, False)
                    img = pg.transform.scale(image, (self.TILE_SIZE, self.TILE_SIZE))
                    imgRect = pg.Rect(col_index * self.TILE_SIZE, row_index * self.TILE_SIZE, self.TILE_SIZE, self.TILE_SIZE)
                    tile = (img, imgRect, self.get_image(tile, True))
                    self.tileList.append(tile)