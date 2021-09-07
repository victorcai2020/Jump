from random import choice

TITLE = "Jump!"
WIDTH = 480
HEIGHT = 600
FPS = 60
FONT = 'arial'
HS_FILE = 'highscore.txt'
SPRITESHEET = 'spritesheet_jumper.png'

PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8
PLAYER_JUMP = 25

BOOST_POWER = 80
POW_SPAWN_PCT = 7
MOB_FREQ = 5000
PLAYER_LAYER = 2
PLATFORM_LAYER = 1
POW_LAYER = 1
MOB_LAYER = 2
CLOUD_LAYER = 0
CLOUD_LIST = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
CLOUD_DIST = choice(CLOUD_LIST)


PLATFORM_LIST = [(10, HEIGHT - 60),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4 - 50),
                 (125, HEIGHT - 350),
                 (350, 200),
                 (175, 100)]

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BGCOLOR = 51, 153, 255
