#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import COLOR_WHITE, MENU_OPTION, EVENT_ENEMY
from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, menu_option):
        self.window: Surface = window
        self.name = name
        self.mode = menu_option  # Opção do Menu
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))  # Extend, pois retorna uma lista
        self.entity_list.append(EntityFactory.get_entity('Player1'))  # Append, pois retorna um único objeto
        if menu_option in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))
        pygame.time.set_timer(EVENT_ENEMY, 8000)

    def run(self):
        pygame.mixer_music.load(f'./asset/{self.name}.flac')
        pygame.mixer_music.play(1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)  # Aqui eu desenho minhas entidades
                self.level_text(14, f'Fps: {clock.get_fps() :.0f}', COLOR_WHITE, (10, 10))
                ent.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
            pygame.display.flip()
        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, texto_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=texto_pos[0], top=texto_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)

