terrain_tiles_path = "./graphics/terrain/terrain_tiles.png"

gold_folder_path = "./graphics/coins/gold"
silver_folder_path = "./graphics/coins/silver"

enemy_folder_path = ["./graphics/enemy/run/br9l", "./graphics/enemy/run/Fer3awn"]
end_path = "./graphics/character/hat.png"
run_folder_path = "./graphics/character/dust_particles/run"
character_folder_path = "./graphics/character/"
jump_folder_path = "./graphics/character/dust_particles/jump"
land_folder_path = "./graphics/character/dust_particles/land"
explosion_folder_path = "./graphics/enemy/explosion"


def getpath(path):
    """
    Obtient le chemin d'accès complet vers une image spécifique dans le dossier 'graphics/Buttons/'.

    Args:
    - path (str): Nom du fichier image sans extension.

    Returns:
    - str: Chemin d'accès complet vers l'image spécifiée, prêt à être utilisé.
    """
    return f"graphics/Buttons/{path}.png"


logo = "./graphics/images/Logo.png"
