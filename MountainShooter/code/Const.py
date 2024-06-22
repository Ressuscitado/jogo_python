import pygame

# C
COLOR_ORANGE = (255, 128, 0)
COLOR_YELLOW = (255, 255, 128)
COLOR_WHITE = (255, 255, 255)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {'Level1Bg0': 0,
                'Level1Bg1': 1,
                'Level1Bg2': 2,
                'Level1Bg3': 3,
                'Level1Bg4': 4,
                'Level1Bg5': 5,
                'Level1Bg6': 6,
                'Player1': 3,
                'Player2': 3,
                'Enemy1': 1,
                'Enemy2': 2
                }

# M
MENU_OPTION = ('NEW GAME',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'EXIT')

# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324
