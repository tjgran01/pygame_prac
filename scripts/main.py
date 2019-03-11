import pygame
import sys
from pygame.locals import *

control_dict = {"Left": 276,
                "Right": 275,
                "Down": 274,
                "Up": 273}

tile_size = 32
tile_array_dims = (12, 8)
window_mod = 2
sprite_mod = window_mod * 2
screen_x = tile_size * tile_array_dims[0] * window_mod
screen_y = tile_size * tile_array_dims[1] * window_mod

pygame.init()
DISPLAYSURF = pygame.display.set_mode((screen_x, screen_x))
pygame.display.set_caption("Battle Prototype")

grass_img = pygame.image.load('../art/32_pixel_ground/grass_center.png').convert()
img_size = grass_img.get_size()
grass_img = pygame.transform.scale(grass_img, (int(img_size[0]*sprite_mod), int(img_size[1]*sprite_mod)))
start_x = 0
start_y = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == 2:
            print(event.key)
            if event.key == control_dict["Left"]:
                start_x -= 32
            elif event.key == control_dict["Right"]:
                start_x += 32
            elif event.key == control_dict["Up"]:
                start_y -= 32
            elif event.key == control_dict["Down"]:
                start_y += 32
            DISPLAYSURF.fill((0,0,0))
            DISPLAYSURF.blit(grass_img, (start_x, start_y))
        pygame.display.update()
