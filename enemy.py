import pygame
from tiles import AnimatedTile
from path import enemy_folder_path
from random import choice


class Enemy(AnimatedTile):
    """
    Classe représentant un ennemi animé.

    Hérite de la classe AnimatedTile.

    Attributes:
    size (tuple): Taille de l'ennemi.
    x (int): Position horizontale initiale de l'ennemi.
    y (int): Position verticale initiale de l'ennemi.

    Methods:
    __init__: Initialise un objet ennemi.
    move: Déplace l'ennemi horizontalement.
    reverse_image: Inverse l'image de l'ennemi en fonction de sa direction de déplacement.
    reverse: Inverse la direction de déplacement de l'ennemi.
    update: Met à jour la position de l'ennemi sur l'écran.
    """

    def __init__(self, size, x, y):
        """
        Initialise un objet ennemi.

        Args:
        size (tuple): Taille de l'ennemi.
        x (int): Position horizontale initiale de l'ennemi.
        y (int): Position verticale initiale de l'ennemi.

        Returns:
        None
        """
        self.choice = choice([0, 1])
        super().__init__(size, x, y, enemy_folder_path[self.choice], 1.6)
        self.rect.y += size - self.image.get_size()[1]
        self.speed = 3

    def move(self):
        """
        Déplace l'ennemi horizontalement.

        Returns:
        None
        """
        self.rect.x += self.speed

    def reverse_image(self):
        """
        Inverse l'image de l'ennemi en fonction de sa direction de déplacement.

        Returns:
        None
        """
        if self.speed <= 0:
            self.image = pygame.transform.flip(self.image, True, False)

    def reverse(self):
        """
        Inverse la direction de déplacement de l'ennemi.

        Returns:
        None
        """
        self.speed *= -1

    def update(self, screen_direction):
        """
        Met à jour la position de l'ennemi sur l'écran.

        Args:
        screen_direction (int): Direction du déplacement de l'écran.

        Returns:
        None
        """
        self.rect.x += screen_direction
        self.animate()
        self.move()
        self.reverse_image()
