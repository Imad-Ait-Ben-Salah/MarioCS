import pygame
from images_importings import import_images


class Tile(pygame.sprite.Sprite):
    """
    Classe de base représentant une tuile générique dans le jeu.

    Attributes:
        image (Surface): La surface de la tuile.
        rect (Rect): La zone rectangulaire occupée par la tuile.

    Methods:
        update(deplacement): Met à jour la position de la tuile en fonction du déplacement actuel.
    """

    def __init__(self, size, x, y):
        """
        Initialise un objet Tile.

        Args:
            size (int): Taille de la tuile (en pixels).
            x (int): Coordonnée x initiale de la tuile.
            y (int): Coordonnée y initiale de la tuile.
        """
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self, deplacement):
        """
        Met à jour la position de la tuile en fonction du déplacement actuel.

        Args:
            deplacement (int): La valeur de déplacement horizontale actuelle.
        """
        self.rect.x += deplacement


class StaticTile(Tile):
    """
    Classe représentant une tuile statique dans le jeu.

    Attributes:
        image (Surface): La surface de la tuile statique.

    Inherits:
        Tile: Classe de base pour une tuile générique.
    """

    def __init__(self, size, x, y, surface):
        """
        Initialise un objet StaticTile.

        Args:
            size (int): Taille de la tuile (en pixels).
            x (int): Coordonnée x initiale de la tuile.
            y (int): Coordonnée y initiale de la tuile.
            surface (Surface): Surface représentant l'image de la tuile statique.
        """
        super().__init__(size, x, y)
        self.image = surface


class AnimatedTile(Tile):
    """
    Classe représentant une tuile animée dans le jeu.

    Attributes:
        frames (list): Liste des images pour l'animation de la tuile.

    Inherits:
        Tile: Classe de base pour une tuile générique.
    """

    def __init__(self, size, x, y, path, scale=1):
        """
        Initialise un objet AnimatedTile.

        Args:
            size (int): Taille de la tuile (en pixels).
            x (int): Coordonnée x initiale de la tuile.
            y (int): Coordonnée y initiale de la tuile.
            path (str): Chemin vers le répertoire contenant les images pour l'animation.
            scale (int, optional): Facteur d'échelle pour les images animées (par défaut: 1).
        """
        super().__init__(size, x, y)
        self.frames = import_images(path)
        scaled_images = [
            pygame.transform.scale(
                image, (image.get_width() * scale, image.get_height() * scale)
            )
            for image in self.frames
        ]
        self.frames = scaled_images
        self.frame_index = 0
        self.image = self.frames[self.frame_index]

    def animate(self):
        """Anime la tuile en faisant défiler les images dans la liste frames."""
        self.frame_index += 0.15
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]

    def update(self, deplacement):
        """
        Met à jour la position de la tuile en fonction du déplacement actuel et anime la tuile.

        Args:
            deplacement (int): La valeur de déplacement horizontale actuelle.
        """
        self.animate()
        self.rect.x += deplacement


class Coin(AnimatedTile):
    """
    Classe représentant une pièce (coin) animée dans le jeu.

    Attributes:
        val (int): La valeur numérique de la pièce.

    Inherits:
        AnimatedTile: Classe pour une tuile animée.
    """

    def __init__(self, size, x, y, path, val):
        """
        Initialise un objet Coin.

        Args:
            size (int): Taille de la pièce (en pixels).
            x (int): Coordonnée x initiale de la pièce.
            y (int): Coordonnée y initiale de la pièce.
            path (str): Chemin vers le répertoire contenant les images pour l'animation de la pièce.
            val (int): La valeur numérique de la pièce.
        """
        super().__init__(size, x, y, path)
        center_x = x + int(size / 2)
        center_y = y + int(size / 2)
        self.rect = self.image.get_rect(center=(center_x, center_y))
        self.val = val
