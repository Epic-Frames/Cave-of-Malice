import pygame as pg

class Enemy():
    def __init__(self, enemyType, x, y, width, height, speed, health, sourceImage, direction):
        self.type = enemyType
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.health = health


        self.direction = direction

        self.sourceImage = sourceImage
    
        self.image = pg.image.load(self.sourceImage)
        self.image = pg.transform.scale(self.image, (self.width, self.height))

        self.mask = pg.mask.from_surface(self.image)


    def move(self, x1, x2):
        if self.type == "Spider":
            self.x += self.speed * self.direction
            if self.x <= x1:
                self.direction = 1
            elif self.x >= x2:
                self.direction = -1

    
    def check_alive(self):
        if self.health <= 0:
            return False
        return True
    

    def clear_enemy(self):
        self.x = -500
    

    def take_damage(self, damage):
        self.health -= damage
    

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))