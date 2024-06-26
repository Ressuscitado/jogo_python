#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import C_WHITE, MENU_OPTION, EVENT_ENEMY, WIN_HEIGHT, C_GREEN, C_CYAN, EVENT_TIMEOUT
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:
    def __init__(self, window: Surface, name: str, menu_option: str, player_score: list[int]):
        self.window = window
        self.name = name
        self.mode = menu_option  # Opção do Menu
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))  # Extend, pois retorna uma lista
        player = EntityFactory.get_entity('Player1')
        player.score = player_score[0]  # Score player1
        self.entity_list.append(player)  # Append, pois retorna um único objeto
        if menu_option in [MENU_OPTION[1], MENU_OPTION[2]]:
            player = EntityFactory.get_entity('Player2')
            player.score = player_score[1] # Score player2
            self.entity_list.append(player)
        pygame.time.set_timer(EVENT_ENEMY, 1000)
        self.timeout = 40000  # 20 segundos de fase
        pygame.time.set_timer(EVENT_TIMEOUT, 100)  # 100 ms

    def run(self, player_score: list[int]):
        pygame.mixer_music.load(f'./asset/{self.name}.flac')
        pygame.mixer_music.set_volume(0.3)
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)  # Aqui eu desenho minhas entidades
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
                if ent.name == 'Player1':
                    self.level_text(14, f'Player1: - Healthy: {ent.health} | Score: {ent.score}', C_GREEN, (10, 25))
                if ent.name == 'Player2':
                    self.level_text(14, f'Player2: - Healthy: {ent.health} | Score: {ent.score}', C_CYAN, (10, 45))

            #  FPS desenhado na tela
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', C_WHITE, (10, 5))
            self.level_text(14, f'Fps: {clock.get_fps() :.0f}', C_WHITE, (10, WIN_HEIGHT - 35))
            #  Atualizar tela
            pygame.display.flip()
            #  Verificar relacionamentos entre entidades
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

            #  Conferir eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

                if event.type == EVENT_TIMEOUT:
                    self.timeout -= 100  # Começa com 20000
                    if self.timeout == 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'Player1':
                                player_score[0] = ent.score
                            if isinstance(ent, Player) and ent.name == 'Player2':
                                player_score[1] = ent.score
                        return True

                found_player = False
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        found_player = True

                if not found_player:
                    return False

    def level_text(self, text_size: int, text: str, text_color: tuple, texto_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=texto_pos[0], top=texto_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)

