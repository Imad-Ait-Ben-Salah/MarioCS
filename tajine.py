import pygame


class Tajine(pygame.sprite.Sprite):
    """
    Classe représentant un tajine, projectile tiré par le personnage.

    Attributes:
        speed (int): La vitesse du projectile.
        direction (int): La direction du déplacement du projectile (gauche : -1, droite : 1).
        image (Surface): L'image représentant le tajine.
        rect (Rect): La zone rectangulaire occupée par l'image du tajine.

    Methods:
        go(): Déplace le tajine dans sa direction actuelle en fonction de sa vitesse.
        update(deplacement): Met à jour la position du tajine en fonction du déplacement actuel.
    """

    def __init__(self, x, y, direction):
        """
        Initialise un objet Tajine.

        Args:
            x (int): Coordonnée x initiale du tajine.
            y (int): Coordonnée y initiale du tajine.
            direction (int): La direction initiale du déplacement du tajine (gauche : -1, droite : 1).
        """
        super().__init__()
        self.speed = 10
        self.direction = direction
        self.image = pygame.image.load(
            "./graphics/character/tajine.png"
        ).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def go(self):
        """
        Fait avancer le tajine dans sa direction actuelle en fonction de sa vitesse.
        """
        self.rect.x += self.direction * self.speed

    def update(self, deplacement):
        """
        Met à jour la position du tajine en fonction du déplacement actuel.

        Args:
            deplacement (int): La valeur de déplacement horizontale actuelle.
        """
        self.rect.x += deplacement
