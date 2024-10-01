# MarioCS

## Membres du projet
- Bheddar Zakaria (zakaria.bheddar@student-cs.fr)
- Ait Ben Salah	Imad (imad.ait-ben-salah@student-cs.fr)
- El Hachimi Adam (adam.el-hachimi@student-cs.fr)
- Bihi Mohammed Yassine (mohammedyassine.bihi@student-cs.fr)
- Messioui Yassine (yassine.messioui@student-cs.fr)
- Boumoussou Younes-Jihad (younes.boumoussou@student-cs.fr)

## Description
MarioCS est un jeu d'aventure inspiré du célèbre jeu vidéo Mario, développé dans le cadre d'un projet collaboratif aux Coding Weeks de CentraleSupélec. Le but du jeu est d'atteindre une destination située dans une carte de parcours. Pour cela, vous devrez parcourir une carte parsemée d'ennemis appelés BR9EL ou FIR3AWN. Le défi principal est d'atteindre la destination avec le plus grand score possible.

Le jeu contient actuellement deux niveaux de difficulté : facile et difficile. Votre objectif est de terminer la carte avec le meilleur score possible tout en évitant les ennemis et en utilisant vos compétences pour surmonter les obstacles.

## Origine du nom "MarioCS"

"**MarioCS**" représente la fusion entre le jeu vidéo "Mario" et des éléments de la culture marocaine. Ce nom a été choisi pour un projet de jeu développé lors des Coding Weeks de CentraleSupélec (CS). Il vise à intégrer les éléments iconiques de "Mario" avec des influences visuelles et thématiques inspirées du Maroc.

Cette désignation exprime la combinaison entre les références classiques de "Mario" et les aspects culturels marocains, soulignant ainsi la singularité du projet au sein de CentraleSupélec.



## Calcul du score

Le calcul du score est basé sur différentes actions du joueur :
- Chaque Gold ramassé rapporte 20 points (P_Gold = 20).
- Chaque Silver ramassé rapporte 5 points (P_Silver = 5).
- Pour chaque ennemi tué, le joueur gagne 10 points (P_Enemy = 10).
- Pour chaque attaque ennemie subie, le joueur perd 100 points (P_Attaque = -100).
- À la fin du jeu, le joueur reçoit une bonification en fonction du nombre de cœurs restants multiplié par 100 (Bonus_Coeurs = N_Coeurs * 100).

Le score total (Score_Total) se calcule selon la formule suivante :
Score_Total = max[(20 * Nombre_de_Gold) + (5 * Nombre_de_Silver) + (10 * Nombre_d_ennemis_tués) - (100 * Nombre_d_attaques_subies) + (100 * Nombre_de_cœurs_restants), 0]

Cette formule permet d'établir un score global représentatif des actions du joueur tout au long du jeu, récompensant à la fois la collecte d'objets précieux, la victoire sur les ennemis, mais également prenant en compte les pénalités pour les attaques subies.

De plus, le jeu enregistre le high score. Pour consulter votre score actuel, vous pouvez le suivre en jouant ou à la fin du jeu (un win) où votre score et votre high score seront affichés.


## Installation des dépendances
Pour installer les dépendances nécessaires, suivez les étapes suivantes :

1. Assurez-vous d'avoir Python installé sur votre système. Si ce n'est pas le cas, téléchargez et installez Python depuis [le site officiel](https://www.python.org/).
2. Clonez ce dépôt Git sur votre machine en utilisant la commande suivante :
    ```
    git clone https://gitlab-cw1.centralesupelec.fr/zakaria.bheddar/projet_jeu.git
    ```
3. Accédez au répertoire du projet :
    ```
    cd projet_jeu
    ```
4. Installez les dépendances requises en exécutant la commande suivante :
    ```
    pip install -r requirements.txt
    ```

## Lancement du jeu
Une fois les dépendances installées, vous pouvez lancer le jeu en suivant ces étapes :

1. Assurez-vous d'être dans le répertoire du projet MarioCS.
2. Exécutez la commande suivante pour lancer le jeu :
    ```
    python main.py
    ```

## Comment jouer
Pour jouer :
- Utilisez les touches directionnelles pour vous déplacer.
    - **Gauche**: flèche directionnelle gauche ou "Q".
    - **Droite**: flèche directionnelle droite ou "D".
    - **Sauter**: flèche directionnelle vers le haut ou "Z".
- Utilisez la touche "Espace" pour lancer un TAJINE (tir) et éliminer les ennemis BR9EL ou FIR3AWN.
- Utilisez la touche "P" pour pauser le jeu.
- Vous disposez de trois cœurs. Si un ennemi vous touche, vous perdrez un cœur. Assurez-vous de ne pas perdre tous vos cœurs avant d'atteindre la destination.


## MVP (Minimum Viable Product)
Avant de commencer le développement du projet MarioCS, nous avons réalisé un MVP simple avec des fonctionnalités de base, comprenant :
- Un personnage sous forme de boîte (placeholder) se déplaçant dans une carte 2D.
- Implémentation de collisions basiques (collision verticale, collision horizontale ...).
- Ajout de la physique élémentaire, incluant la gravité, vitesse, mouvements ...

Ce MVP a servi de base pour le développement ultérieur du jeu MarioCS et aussi pour découvrir le module pygame.

## Tester le MVP
Si vous souhaitez découvrir le MVP et voir les tests effectués pour s'assurer de la logique du jeu, suivez ces étapes pour le lancer :

1. Suivre les étapes précédentes de l'installation des dépendances.
2. Assurez-vous bien d'être dans le dossier projet_jeu, puis accédez au répertoire du MVP :
    ```
    cd mvp+test
    ```
3. Exécutez la commande suivante pour lancer le jeu MVP :
    ```
    python main.py
    ```
4. Pour tester l'ensemble du code du MVP, exécutez la commande suivante :
    ```
    pytest
    ```

## Répartition des rôles

Dans le cadre de ce projet, chacun des membres a contribué au développement global du jeu, avec des domaines de spécialisation. Voici un résumé des tâches dominantes de chaque membre :

- **Bheddar Zakaria** :
    - Gestion de la logique du jeu, développement et correction de bugs.
    - Coordination et adaptation du travail des autres membres pour l'intégration fonctionnelle.

- **Ait Ben Salah Imad** :
    - Graphisme et création de textures pour le jeu.
    - Création de maps, travail avec Tiled et contribution à la conception visuelle.

- **El Hachimi Adam** :
    - Gestion des sons, utilisation de Tiled et lecture des fichiers CSV.
    - Contribution aux éléments sonores et à l'intégration de ressources externes.

- **Bihi Mohammed Yassine** :
    - Affichage du score, santé, monnaie et gestion des objets spéciaux.
    - Proposition du nom du jeu et contribution à la mécanique du jeu.

- **Messioui Yassine** :
    - Interface utilisateur, menus, et gestion des boutons.
    - Implémentation des menus de pause, gestion de l'entrée dans les niveaux et éléments graphiques.

- **Boumoussou Younes-Jihad** :
    - Création du rapport et de la présentation du projet.
    - Tests pour la phase MVP, contribution à la logique du jeu et coordination des travaux.

Bien que chaque membre ait eu des tâches principales, tous étaient impliqués dans les discussions et le soutien pour chaque partie du jeu. Chacun était disposé à aider les autres membres en cas de besoin, assurant ainsi une collaboration harmonieuse tout au long du projet.

# Structure des fichiers du Projet MarioCS

Ce projet comprend plusieurs fichiers Python et répertoires organisés pour implémenter diverses fonctionnalités du jeu MarioCS. Voici une vue d'ensemble de chaque fichier et répertoire :

## Fichiers Python

### `audio.py`
Ce fichier contient les fonctionnalités de gestion des éléments audio du jeu.

### `button.py`
Le fichier `button.py` gère la création et l'interaction avec les boutons de l'interface utilisateur du jeu.

### `enemy.py`
Le fichier `enemy.py` implémente la logique des ennemis présents dans le jeu MarioCS.

### `game_data.py`
`game_data.py` stocke les données des levels du jeu.

### `gui.py`
`gui.py` s'occupe de la création et de la gestion de l'interface graphique utilisateur du jeu.

### `images_importings.py`
Ce fichier contient des fonctionnalités pour importer et gérer les images utilisées dans le jeu.

### `level.py`
Le fichier `level.py` définit les classes et les mécanismes nécessaires à la création et à la gestion des niveaux de jeu.

### `particles.py`
`particles.py` gère les particules utilisées pour des effets visuels spéciaux dans le jeu.

### `path.py`
`path.py` définit les chemins et répertoires relatifs pour accéder aux ressources du jeu.

### `player.py`
Ce fichier implémente les fonctionnalités liées au personnage principal (le joueur) du jeu.

### `read_score.py`
`read_score.py` permet de lire et de récupérer les scores enregistrés dans le fichier `score.csv`.

### `settings.py`
`settings.py` contient les paramètres et configurations du jeu.

### `tajine.py`
`tajine.py` gère les tajines, une fonctionnalité d'attaque du personnage principal contre les ennemis.

### `tiles.py`
Le fichier `tiles.py` définit les tuiles utilisées pour construire les niveaux et les décors du jeu.

### `traitement_csv.py`
`traitement_csv.py` offre des fonctionnalités pour traiter et manipuler des fichiers CSV utilisés dans le jeu.

## Répertoires

### `graphics/`
Le répertoire `graphics/` contient les images, sprites et autres ressources graphiques utilisées dans le jeu.

### `levels/`
`levels/` stocke les données et fichiers relatifs aux différents niveaux de jeu.

### `music/`
Le répertoire `music/` contient les fichiers audio utilisés pour la musique du jeu.

### `videos/`
Le répertoire `videos/` contient les gameplays du jeu MarioCS.

### `mvp+test/`
`mvp+test/` comprend le code source pour le MVP (Minimum Viable Product) du jeu, ainsi que les fichiers de test du MVP.

### `rapport+présentation/`
Le répertoire `rapport+présentation/` inclut le rapport complet et la présentation du projet MarioCS.

## Autres fichiers et ressources

### `main.py`
Le fichier `main.py` est le point d'entrée du jeu MarioCS.

### `requirements.txt`
`requirements.txt` spécifie les dépendances et les modules Python nécessaires pour exécuter le jeu.

### `score.csv`
`score.csv` stocke les scores enregistrés par les joueurs.

### `setup.py`
`setup.py` contient des fonctions pour gérer l'interface utilisateur jeu et gestion des transitions entre menu et level et pause.

Ces fichiers et répertoires contribuent à différentes parties du jeu MarioCS, offrant diverses fonctionnalités et fonctionnements essentiels.


## Vidéo de présentation et Gameplay

- **Vidéo de Gameplay :** [Regarder la vidéo de gameplay de MarioCS et aussi MVP](https://drive.google.com/file/d/1DMX1psy7kyMLHYCqENv0axHB0d8Ex7F6/view?usp=sharing)


## Liens vers le rapport complet et la présentation
Pour une documentation plus détaillée sur le projet, y compris des informations sur le développement, les tests effectués, les choix de conception, et bien plus encore, veuillez consulter notre rapport complet au format PDF.

[Télécharger le rapport PDF](./rapport+présentation/Rapport_jeu_MarioCS.pdf)

[Télécharger la présentation PDF](./rapport+présentation/Présentation_jeu_MarioCS.pdf)


Ce rapport fournit une vue d'ensemble complète du projet MarioCS, détaillant les aspects techniques, les processus de développement et les choix stratégiques pris tout au long du cycle de création du jeu.
