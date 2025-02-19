import pygame as pg
import sys
from enemy import Enemy
from text import Text
from player import Player
from screen import Screen
from world import World

pg.init()

TILE_SIZE = 32
SCREEN_X = 1280
SCREEN_Y = 720
SCREEN = pg.display.set_mode((SCREEN_X, SCREEN_Y))
world = World("Assets/dirt.jpeg", "Assets/lava.jpeg", TILE_SIZE)
screen = Screen(1280, 720)
pg.display.set_caption("Cave of Malice v0.0.0 - alpha")
clock = pg.time.Clock()

player = Player(100, 572, 45, 100, 5, 2, "Assets/player.png", None, 1, -20, 10)

font = pg.font.Font(None, 36)
startupFont = pg.font.Font(None, 56)

level = screen.load_map("level1.txt")

studioText = Text(None, None, "Epic Frame Studio", startupFont, (250, 250, 250), SCREEN_X, SCREEN_Y)
deathText = Text(None, None, "You died!", font, (250, 0, 0), SCREEN_X, SCREEN_Y)
winText = Text(None, None, "You Win", font, (0, 250, 0), SCREEN_X, SCREEN_Y)

# Load assets
currentPage = "start_animation"

FPS = 30

enemy1 = Enemy("Spider", 200, 572, 45, 100, 3, 2, "Assets/player.png", 1)

enemies = []
running = True

enemies.append(enemy1)

def width():
    print("2 point perspective")

def start_animation():
    startTime = pg.time.get_ticks()
    duration = 4000
    frame, halfFrames = None, None
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_m:
                    return "start_page"

        SCREEN.fill((0, 0, 0))

        if frame or halfFrames != 0:
            frame, halfFrames = studioText.blink(SCREEN, duration / 1000 - 1.5, frame, halfFrames, 1500, pg.time.get_ticks())
        

        if pg.time.get_ticks() - startTime > duration:
            return "game"


        pg.display.update()
        clock.tick(FPS)

def game():
    global running
    world.load_tiles(level)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        
        SCREEN.fill((150, 150, 150))

        # Move character
        player.move(world.tileList, SCREEN)
        enemy1.move(32, 500)


        # Detect collision
        if player.check_collision(enemies):
            deathText.show(SCREEN)
            running = False

        # Check winning
        if player.x > enemy1.x and running:
            winText.show(SCREEN)
        

        # Display character
        player.draw(SCREEN)
        enemy1.draw(SCREEN)
        # Display blocks
        world.draw_map(SCREEN)

        clock.tick(FPS)
        pg.display.update()
        
def main():
    global currentPage
    while True:
        # if currentPage == "start_animation":
        #     currentPage = start_animation()
        # if currentPage == "game":
        #     currentPage = game()
        game()

if __name__ == "__main__":
    main()