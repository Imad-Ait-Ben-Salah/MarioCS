from traitement_csv import import_csv_layout
import csv


def read_high_score(level):
    """
    Lit le meilleur score enregistré pour un niveau spécifique.

    Args:
    - level (int): Le numéro du niveau pour lequel récupérer le meilleur score.

    Returns:
    - int: Meilleur score pour le niveau donné.
    """
    data = import_csv_layout("./score.csv")
    return int(data[level + 1][1])


def change_score(level, score):
    """
    Modifie le score pour un niveau donné s'il est supérieur au score actuel.

    Args:
    - level (int): Le numéro du niveau pour lequel changer le score.
    - score (int): Le nouveau score à enregistrer pour le niveau.

    Modifie le fichier score.csv s'il y a un nouveau meilleur score pour le niveau spécifié.
    """
    data = import_csv_layout("./score.csv")
    if score > int(data[level + 1][1]):
        data[level + 1][1] = str(score)
        with open("score.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(data)
