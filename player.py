import pygame
from settings import GRAVITY, vitesse_joueur, jump_speed
from images_importings import import_images
from path import run_folder_path, character_folder_path
from audio import *


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, surface, jump_particules):
        """
        Initialise un objet Player.

        Args:
        - x (int): Position x initiale du joueur.
        - y (int): Position y initiale du joueur.
        - surface (pygame.Surface): Surface d'affichage du joueur.
        - jump_particules (function): Fonction pour générer des particules de saut.
        """
        super().__init__()
        self.import_character_assets()
        self.import_dust_run_particles()
        self.frame_index = 0
        self.animation_speed = 0.1
        self.dust_frame_index = 0
        self.display_surface = surface
        self.dust_animation_speed = 0.1
        self.image = self.animations["idle"][self.frame_index]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.v = vitesse_joueur
        self.gravity = GRAVITY
        self.direction = pygame.math.Vector2(0, 0)
        self.jump_speed = jump_speed
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.face = "right"
        self.terre = False
        self.jump_particules = jump_particules

    def import_dust_run_particles(self):
        """
        Importe les images de particules de poussière pour l'animation de course.
        """
        images = import_images(run_folder_path)
        scale = 2
        scaled_images = [
            pygame.transform.scale(
                image, (image.get_width() * scale, image.get_height() * scale)
            )
            for image in images
        ]
        self.dust_run_particles = scaled_images

    def run_dust_animation(self):
        """
        Anime les particules de poussière lorsque le joueur court.
        """
        if self.status == "run" and self.terre:
            self.dust_frame_index += self.dust_animation_speed
            if self.dust_frame_index >= len(self.dust_run_particles):
                self.dust_frame_index = 0

            dust_particle = self.dust_run_particles[int(self.dust_frame_index)]

            if self.face == "right":
                pos = self.rect.bottomleft - pygame.math.Vector2(20, 20)
                self.display_surface.blit(dust_particle, pos)
            else:
                pos = self.rect.bottomright - pygame.math.Vector2(-15, 20)
                flipped_dust_particle = pygame.transform.flip(
                    dust_particle, True, False
                )
                self.display_surface.blit(flipped_dust_particle, pos)

    def animate(self):
        """
        Anime le joueur en fonction de son état (immobile, course, saut, chute).
        """
        animation = self.animations[self.status]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        image = animation[int(self.frame_index)]
        if self.face == "right":
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image, True, False)
            self.image = flipped_image

    def import_character_assets(self):
        """
        Importe les images pour les différentes animations du personnage.
        """
        character_path = character_folder_path
        self.animations = {"idle": [], "run": [], "jumping": [], "fall": []}
        scale = 3.5
        for animation in self.animations.keys():
            full_path = character_path + animation
            animation_images = import_images(full_path)
            scaled_images = [
                pygame.transform.scale(
                    image, (image.get_width() * scale, image.get_height() * scale)
                )
                for image in animation_images
            ]
            self.animations[animation] = scaled_images

    def jump(self):
        """
        Fait sauter le joueur en modifiant sa vitesse verticale.
        """
        self.direction.y = self.jump_speed

    def apply_gravity(self):
        """
        Applique la gravité pour simuler la chute du joueur.
        """
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def entree_joueur(self):
        """
        Gère les entrées clavier du joueur pour déplacer et sauter.
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_q]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0
        if keys[pygame.K_UP] or keys[pygame.K_z]:
            if self.terre:
                music("./music/Marioc_jump.wav", 0.01)
                self.jump()
                self.jump_particules(
                    self.rect.midbottom,
                )

    def etat_joueur(self):
        """
        Détermine l'état actuel du joueur (immobile, course, saut, chute).
        """
        if self.direction.y < 0:
            self.status = "jumping"
        elif self.direction.y > self.gravity:
            self.status = "fall"
        elif self.direction.x != 0:
            if self.direction.x == 1:
                self.face = "right"
            else:
                self.face = "left"
            self.status = "run"
        else:
            self.status = "idle"
            if not self.terre:
                self.status = "fall"

    def update(self):
        """
        Met à jour les mouvements et animations du joueur en fonction de ses actions et de son état.
        """
        self.entree_joueur()
        self.etat_joueur()
        self.animate()
        self.run_dust_animation()
