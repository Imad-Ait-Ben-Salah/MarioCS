import pygame
from settings import cd_but


# Classe bouton
class Button:
    cd = 0

    def __init__(self, x, y, image, scale):
        """
        Initialise un objet bouton.

        Args:
        x (int): Position horizontale du bouton sur l'écran.
        y (int): Position verticale du bouton sur l'écran.
        image (pygame.Surface): Image représentant le bouton.
        scale (float): Échelle de redimensionnement de l'image du bouton.

        Returns:
        None
        """
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(
            image, (int(width * scale), int(height * scale))
        )
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.pos = pygame.mouse.get_pos()

    def draw(self, surface):
        """
        Dessine le bouton sur la surface spécifiée.

        Args:
        surface (pygame.Surface): Surface sur laquelle le bouton est dessiné.

        Returns:
        bool: Indique si le bouton a été cliqué ou non.
        """
        action = False
        Button.cd += 1
        if Button.cd > cd_but:
            self.pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(self.pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                Button.cd = 0
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action
