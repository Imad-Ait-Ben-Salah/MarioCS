import pygame

GRAVITY = 1
vitesse_joueur = 6
nom_jeu = "Marioc"
jump_speed = -20

fps = 60


level_map = [
    "                            ",
    "                            ",
    "    P                       ",
    "                            ",
    "                            ",
    "                 XX         ",
    "                 XX         ",
    "       X   XXXXXXXXX  XX    ",
    "       X    XX    XX  XXX   ",
    "    XXXX    XXXX  XX  XXXX  ",
    "XXXXXXXX    XXXX  XX  XXXX  ",
]


tile_size = 64
screen_height = len(level_map) * tile_size
screen_width = 1000
