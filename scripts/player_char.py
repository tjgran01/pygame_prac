import os
import sys
import pygame as pg

class Player(pygame.sprite.Sprite):
    def __init__(controller=1, size_mod=2):
        self.controller = controller
        self.image = pg.image.load("../art/guy.png")
        self.size = self.image.get_size()
        self.resized = pg.transform.scale(self.image, (int(self.size[0]*size_mod), int(self.size[1]*size_mod)))
        self.spawn_point = (0, 0)
        self.current_loc = spawn_point

    def spawn_player(DISPLAYSURF):
        DISPLAYSURF.blit(self.sprite, self.spawn_point)

    def move_player(DISPLAYSURF, dir, scr_mod):
        if dir == "Right":
            self.current_loc[0] += 32
        elif dir == "Left":
            self.current_loc[0] -= 32
        elif dir == "Up":
            self.current_loc[1] += 32
        elif dir == "Down":
            self.current_loc[1] -= 32

        DISPLAYSURF,blit(self.spritem self.current_loc)
