import pygame

# C
C_CYAN = (0, 128, 128)
C_GREEN = (0, 128, 0)
C_ORANGE = (255, 128, 0)
C_YELLOW = (255, 255, 128)
C_WHITE = (255, 255, 255)


# E
ENTITY_DAMAGE = {'Level1Bg0': 0,
                 'Level1Bg1': 0,
                 'Level1Bg2': 0,
                 'Level1Bg3': 0,
                 'Level1Bg4': 0,
                 'Level1Bg5': 0,
                 'Level1Bg6': 0,
                 'Player1': 1,
                 'Player2': 1,
                 'Player1Shot': 25,
                 'Player2Shot': 20,
                 'Enemy1Shot': 20,
                 'Enemy2Shot': 15,
                 'Enemy1': 1,
                 'Enemy2': 1
                 }
ENTITY_HEALTH = {'Level1Bg0': 999,
                 'Level1Bg1': 999,
                 'Level1Bg2': 999,
                 'Level1Bg3': 999,
                 'Level1Bg4': 999,
                 'Level1Bg5': 999,
                 'Level1Bg6': 999,
                 'Player1': 300,
                 'Player2': 300,
                 'Player1Shot': 1,
                 'Player2Shot': 1,
                 'Enemy1Shot': 1,
                 'Enemy2Shot': 1,
                 'Enemy1': 50,
                 'Enemy2': 60
                 }
ENTITY_SCORE = {'Level1Bg0': 0,
                'Level1Bg1': 0,
                'Level1Bg2': 0,
                'Level1Bg3': 0,
                'Level1Bg4': 0,
                'Level1Bg5': 0,
                'Level1Bg6': 0,
                'Player1': 0,
                'Player2': 0,
                'Player1Shot': 0,
                'Player2Shot': 0,
                'Enemy1Shot': 0,
                'Enemy2Shot': 0,
                'Enemy1': 100,
                'Enemy2': 125
                }
ENTITY_SHOT_DELAY = {'Player1': 15,  # Intervalo de criação de tiro ao pressionar a tecla
                     'Player2': 15,
                     'Enemy1': 150,
                     'Enemy2': 100
                     }
ENTITY_SPEED = {'Level1Bg0': 0,
                'Level1Bg1': 1,
                'Level1Bg2': 2,
                'Level1Bg3': 3,
                'Level1Bg4': 4,
                'Level1Bg5': 5,
                'Level1Bg6': 6,
                'Player1': 3,
                'Player2': 3,
                'Player1Shot': 5,
                'Player2Shot': 3,
                'Enemy1Shot': 2,
                'Enemy2Shot': 2,
                'Enemy1': 1,
                'Enemy2': 1
                }
EVENT_ENEMY = pygame.USEREVENT + 1

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
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL,
                    'Player2': pygame.K_LCTRL}

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324
