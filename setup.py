import pygame
from settings import (
    screen_width,
    screen_height,
    nom_jeu,
    fps,
    transparent_limit,
    transparent_count,
    transparent_count2,
    game_paused,
)
from level import Level
from game_data import level_0, level_1
import button
from path import getpath, logo
from moviepy.editor import VideoFileClip
from pygame import mixer
from gui import *
from read_score import *

pygame.init()
flags = pygame.FULLSCREEN
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(nom_jeu)
clock = pygame.time.Clock()

# music
mixer.init()
mixer.music.load("./music/Marioc.wav")
mixer.music.set_volume(0.05)
mixer.music.play(-1)


scale_x = screen.get_width() / screen_width
scale_y = screen.get_height() / screen_height
# Pause Menu
resume_img = pygame.image.load(getpath("play")).convert_alpha()
mainmenu_img = pygame.image.load(getpath("Menu")).convert_alpha()
resume_button = button.Button(
    screen.get_width() // 2 - resume_img.get_width(),
    screen.get_height() // 4,
    resume_img,
    2,
)
mainmenu_button = button.Button(
    screen.get_width() // 2 - mainmenu_img.get_width(),
    2 * screen.get_height() // 4,
    mainmenu_img,
    2,
)
# Main Menu
quit_img = pygame.image.load(getpath("quit")).convert_alpha()
play_img = pygame.image.load(getpath("play")).convert_alpha()
quit_button = button.Button(
    screen.get_width() // 2 - quit_img.get_width() * 1.5 // 2,
    3 * screen.get_height() // 4 - 10,
    quit_img,
    1.5,
)
play_button = button.Button(
    screen.get_width() // 2 - play_img.get_width(),
    2 * screen.get_height() // 4,
    play_img,
    2,
)
# level menu
level0_img = pygame.image.load(getpath("LV1")).convert_alpha()
level1_img = pygame.image.load(getpath("LV2")).convert_alpha()
back_img = pygame.image.load(getpath("back")).convert_alpha()
level0_button = button.Button(
    screen.get_width() // 2 - level0_img.get_width() // 2,
    screen.get_height() // 6,
    level0_img,
    1,
)
level1_button2 = button.Button(
    screen.get_width() // 2 - level1_img.get_width() // 2,
    2 * screen.get_height() // 6,
    level1_img,
    1,
)
back_button = button.Button(
    0,
    5 * screen.get_height() // 6 - 10,
    back_img,
    1.5,
)
# Win Menu
next_img = pygame.image.load(getpath("play")).convert_alpha()
next_button = button.Button(
    screen.get_width() // 2 - next_img.get_width(),
    3 * screen.get_height() // 6,
    next_img,
    2,
)
mainmenu_button2 = button.Button(
    screen.get_width() // 2 - 1.5 * mainmenu_img.get_width() // 2,
    4.4 * screen.get_height() // 6,
    mainmenu_img,
    1.5,
)

gif_speed = 0.2
gif_path = "./graphics/Buttons/BG.gif"
clip = VideoFileClip(gif_path)
frames = [
    pygame.image.fromstring(frame.tostring(), clip.size, "RGB")
    for frame in clip.iter_frames(fps=clip.fps)
]
frames = [
    pygame.transform.scale(image, (screen_width, screen_height)) for image in frames
]
frame_index = 0
logo_img = pygame.image.load(logo)
logo_img = pygame.transform.scale(
    logo_img, (logo_img.get_width() * 4, logo_img.get_height() * 4)
)

d = {0: level_0, 1: level_1, 2: None}
current_level = 0


def main(num):
    """
    Fonction principale du jeu. Elle gère le déroulement du jeu en fonction du niveau actuel.

    Args:
        num (int): Numéro du niveau en cours.

    Cette fonction initialise le jeu et gère les événements, l'état du jeu, la pause, la victoire,
    le game over, et appelle les différents menus et niveaux du jeu.
    """
    global game_paused
    global transparent_count
    global transparent_count2
    transparent_count2 = 0
    if num == 2:
        game_over()
    level = d[num]
    current_level = num
    isnext = False
    game_paused = False

    levels = Level(level, screen, num)
    is_quit = False
    run = True
    while run:
        death = levels.playerdeath
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    game_paused = not game_paused
                    transparent_count = 0
        if death:
            run = False
        if game_paused:
            s = pygame.Surface((screen.get_width(), screen.get_height()))
            transparent_count += 1
            if transparent_count < transparent_limit:
                s.set_alpha(30)
                s.fill((0, 0, 0))
                screen.blit(s, (0, 0))
            if resume_button.draw(screen):
                game_paused = False
            if mainmenu_button.draw(screen):
                is_quit = True
                run = False
        elif levels.win:
            s = pygame.Surface((screen.get_width(), screen.get_height()))
            transparent_count2 += 1
            if transparent_count2 < transparent_limit:
                s.set_alpha(30)
                s.fill((0, 0, 0))
                screen.blit(s, (0, 0))
            if next_button.draw(screen):
                isnext = True
                run = False
            if mainmenu_button2.draw(screen):
                is_quit = True
                run = False
            current_score = levels.score
            high_score = read_high_score(current_level)
            u = GUI(screen)
            u.show_high_score(high_score, current_score)
        else:
            sahara_sky_color = (255, 200, 130)
            screen.fill(sahara_sky_color)
            levels.run()
            scaled_surface = pygame.transform.scale(
                screen, (int(screen_width * scale_x), int(screen_height * scale_y))
            )
            screen.blit(scaled_surface, (0, 0))
        pygame.display.update()
        clock.tick(fps)

    if isnext:
        num = num + 1
        main(num)
    elif death:
        main(current_level)
    elif is_quit:
        welcome_menu()

    pygame.quit()


def welcome_menu():
    """
    Menu d'accueil du jeu.

    Gère l'écran d'accueil avec les boutons de démarrage et de quitter le jeu.
    """
    global frame_index
    run = True
    is_quit = False

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        screen.blit(frames[int(frame_index)], (0, 0))
        screen.blit(
            logo_img,
            (
                screen.get_width() // 2 - logo_img.get_width() // 2,
                screen.get_height() // 13,
            ),
        )
        if play_button.draw(screen):
            run = False
        if quit_button.draw(screen):
            is_quit = True
            run = False

        pygame.display.update()
        clock.tick(fps)
        frame_index = (frame_index + gif_speed) % len(frames)
    if is_quit:
        pygame.quit()
    else:
        levels()


def levels():
    """
    Menu de sélection des niveaux.

    Gère l'écran de sélection des niveaux du jeu.
    """
    level = 0
    global frame_index
    run = True
    is_quit = False

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        screen.blit(frames[int(frame_index)], (0, 0))
        if level0_button.draw(screen):
            level = 0
            run = False
        if level1_button2.draw(screen):
            level = 1
            run = False
        if back_button.draw(screen):
            run = False
            is_quit = True

        pygame.display.update()
        clock.tick(fps)
    if is_quit:
        welcome_menu()
    else:
        main(level)


def game_over():
    """
    Fonction de gestion de l'écran de Game Over.

    Affiche l'écran de Game Over avec un bouton pour retourner au menu principal.
    """
    run = True
    global frame_index
    global transparent_count2
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        screen.blit(frames[int(frame_index)], (0, 0))
        if mainmenu_button.draw(screen):
            run = False
        u = GUI(screen)
        u.show_Congrats()
        pygame.display.update()
        clock.tick(fps)
        frame_index = (frame_index + gif_speed) % len(frames)
    transparent_count2 = 0
    welcome_menu()
