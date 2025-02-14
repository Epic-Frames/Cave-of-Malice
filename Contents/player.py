import pygame as pg

class Player():
    def __init__(self, x, y, width, height, speed, health, sourceImage, footY, gravity, jumpPower):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.health = health
        self.sourceImage = sourceImage
        self.xChange = 0
        self.yChange = 0
        self.gravity = gravity
        self.jumpPower = jumpPower

        self.rightX = self.x + self.width


        self.jumping = False
        self.on_ground = True

        if y is None:
            self.y = footY - self.height
            self.footY = footY
        elif footY is None:
            self.footY = self.y + self.height

        self.image = pg.image.load(self.sourceImage)
        self.image = pg.transform.scale(self.image, (self.width, self.height))

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.mask = pg.mask.from_surface(self.image)


    def check_walk(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_LEFT] and keys[pg.K_RIGHT]:
            pass
        elif keys[pg.K_LEFT]:
            self.xChange = -self.speed
        elif keys[pg.K_RIGHT]:
            self.xChange = self.speed
        elif keys[pg.K_UP]:
            self.yChange = self.speed
        elif keys[pg.K_DOWN]:
            self.yChange = -self.speed
        
        # if keys[pg.K_UP] and self.on_ground:
        #     self.jumping = True
        #     self.yChange = self.jumpPower
        #     self.on_ground = False
    

    def jump(self):
        # print(self.y, self.yChange)
        self.y -= self.yChange
        # self.yChange -= self.gravity
        # self.footY = self.y + self.height
        # print(self.y, self.yChange)


    def collision(self, tileList):
        playerYRect = pg.Rect(self.x, self.y + self.yChange, self.width, self.height)
        playerXRect = pg.Rect(self.x + self.xChange, self.y, self.width, self.height)

        if pg.Rect.colliderect(playerXRect, tileList[1][1]):
            print("we did it again!")

        # collideTest = pg.Rect.colliderect(playerXRect, pg.Rect(100, 100, 100, 100))
        # if collideTest:
        #     print("we did it")
        # print('playerXRect', playerXRect)
        # print('playerYRect', playerYRect)
        for tile in tileList:
            if pg.Rect.colliderect(playerXRect, tile[1]):
                self.xChange = 0
            # print('tile[1]: ', tile[1])
            # print(self.rect.x, self.rect.y + self.yChange, self.width, self.height)
            if pg.Rect.colliderect(playerYRect, tile[1]):
                print("OK")
                if self.yChange < 0:
                    print(tile[1])
                    print(self.rect.x, self.rect.y - self.yChange, self.width, self.height)
                    self.y = tile[1].top - self.height
                    self.on_ground = True
                    self.yChange = 0
                    print('yChange:', self.yChange)
                    return True
                elif self.yChange > 0:
                    print("NICE")
                    self.y = tile[1].bottom
                    self.yChange = 0
        return self.on_ground
    


    def move(self, tileList):
        self.check_walk()

        if self.xChange != 0:
            self.x += self.xChange
            self.rightX = self.x + self.width
            self.xChange = 0
        
        # Jump logic
        self.jump()

        self.rect.x = self.x
        self.rect.y = self.y
        
        if self.collision(tileList):
            self.yChange = 0
            self.on_ground = True


    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))


    def check_collision(self, enemies):
        for enemy in enemies:
            offsetX = enemy.x - self.x
            offsetY = enemy.y - self.y
            if self.mask.overlap(enemy.mask, (offsetX, offsetY)):
                return True
        return False