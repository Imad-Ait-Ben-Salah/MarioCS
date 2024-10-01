from csv import reader
from settings import tile_size
import pygame


def import_csv_layout(chemin):
    """
    Importe une carte depuis un fichier CSV.

    Arguments :
    - chemin (str) : Le chemin vers le fichier CSV contenant la carte.

    Retour :
    - terrain_map (list) : Une liste bidimensionnelle représentant la carte,
      où chaque élément de la liste contient une ligne de la carte sous forme de liste.
    """
    terrain_map = []
    with open(chemin) as file:
        level = reader(file, delimiter=",")
        for row in level:
            terrain_map.append(list(row))
    return terrain_map


def import_cut_graphics(chemin):
    """
    Découpe une image en tuiles de taille fixe.

    Arguments :
    - chemin (str) : Le chemin vers le fichier image contenant les tuiles.

    Retour :
    - cut_tiles (list) : Une liste d'images (surfaces) représentant chaque tuile
      extraite de l'image source. Chaque tuile est stockée comme une surface pygame dans la liste.
    """
    surface = pygame.image.load(chemin).convert_alpha()
    tile_num_x = int(surface.get_size()[0] / tile_size)
    tile_num_y = int(surface.get_size()[1] / tile_size)
    cut_tiles = []
    for row in range(tile_num_y):
        for col in range(tile_num_x):
            x = col * tile_size
            y = row * tile_size
            new_surf = pygame.Surface((tile_size, tile_size), flags=pygame.SRCALPHA)
            new_surf.blit(surface, (0, 0), pygame.Rect(x, y, tile_size, tile_size))
            cut_tiles.append(new_surf)
    return cut_tiles
