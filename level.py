import pygame
from traitement_csv import import_csv_layout, import_cut_graphics
from settings import tile_size, screen_width, vitesse_joueur, screen_height
from tiles import Tile, StaticTile, Coin
from path import (
    terrain_tiles_path,
    gold_folder_path,
    silver_folder_path,
    end_path,
)
from enemy import Enemy
from player import Player
from particles import ParticleEffect
from random import choice
from audio import *
from tajine import Tajine
from gui import GUI
from read_score import *


class Level:
    def __init__(self, level_data, screen, num):
        """
        Initialise un niveau du jeu avec les données spécifiées.

        Args:
        level_data (dict): Données spécifiques au niveau.
        screen (pygame.Surface): Surface de l'écran.
        num (int): Numéro du niveau.

        Returns:
        None
        """
        # paramètres d'interface
        self.screen = screen
        self.deplacement = 0
        # stats
        self.gui = GUI(screen)

        # player
        player_layout = import_csv_layout(level_data["player"])
        self.player = pygame.sprite.GroupSingle()
        self.goal = pygame.sprite.GroupSingle()
        self.player_setup(player_layout)
        self.idle = False
        self.dust_sprite = pygame.sprite.GroupSingle()
        self.player_on_ground = False
        self.playerdeath = False
        self.player_health = 3
        self.hit = False
        self.count = 0
        self.slowed = False
        self.fact = 1
        self.vitesse_joueur = vitesse_joueur
        self.win = False
        self.attenteplayerdeath = False
        self.temps = 0
        self.attentehitdeath = False
        self.num = num
        self.score = 0
        self.final = False

        # tajine
        self.tajine_sprites = pygame.sprite.Group()
        self.cooldown = 0
        self.tagine = 3

        # terrain
        terrain_layout = import_csv_layout(level_data["terrain"])
        self.terrain_sprites = self.create_tile_group(terrain_layout, "terrain")

        # coins
        coins_layout = import_csv_layout(level_data["coins"])
        self.coins_sprites = self.create_tile_group(coins_layout, "coins")
        self.gold = 0
        self.silver = 0

        # enemy
        enemy_layout = import_csv_layout(level_data["enemies"])
        self.enemy_sprites = self.create_tile_group(enemy_layout, "enemies")

        # constraints
        constraint_layout = import_csv_layout(level_data["constraints"])
        self.constraint_sprites = self.create_tile_group(
            constraint_layout, "constraints"
        )

    def death(self):
        """
        Gère la mort du joueur.

        Returns:
        None
        """
        p = self.player.sprite
        if p.rect.y >= 2 * screen_height:
            self.attenteplayerdeath = True
            music("./music/Marioc_waa.wav", 0.3)
        elif self.player_health <= 0:
            self.attentehitdeath = True
            music("./music/Marioc_killed.wav", 0.2)
        if self.attenteplayerdeath or self.attentehitdeath:
            self.temps += 1
        if self.temps >= 50 and self.attentehitdeath:
            self.playerdeath = True
        if self.temps >= 150 and self.attenteplayerdeath:
            self.playerdeath = True
        if self.playerdeath:
            self.temps = 0
            self.attenteplayerdeath = False
            self.attentehitdeath = False

    def player_setup(self, layout):
        """
        Configure le joueur en fonction de la disposition spécifiée.

        Args:
        layout (list): Disposition du joueur.

        Returns:
        None
        """
        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if val == "0":
                    sprite = Player(x, y, self.screen, self.jump_particules)
                    self.player.add(sprite)
                if val == "1":
                    end_surface = pygame.image.load(end_path).convert_alpha()
                    sprite = StaticTile(tile_size, x, y, end_surface)
                    self.goal.add(sprite)

    def win_situation(self):
        """
        Vérifie si le joueur atteint l'objectif de fin du niveau.
        Met à jour l'état de victoire en fonction de la collision entre le joueur et l'objectif.
        """
        p = self.player.sprite
        g = self.goal.sprite
        u = g.rect.colliderect(p.rect)
        self.win = u

    def create_tile_group(self, layout, type):
        """
        Crée des groupes de sprites en fonction du type (terrain, pièces, ennemis, contraintes).

        Args:
        layout (list): La disposition des sprites dans le niveau.
        type (str): Le type de sprite à créer.

        Returns:
        pygame.sprite.Group: Groupe de sprites créé en fonction du type.
        """
        sprite_group = pygame.sprite.Group()
        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                if val != "-1":
                    sprite = None
                    x = col_index * tile_size
                    y = row_index * tile_size

                    if type == "terrain":
                        terrain_tile_list = import_cut_graphics(terrain_tiles_path)
                        tile_surface = terrain_tile_list[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                    if type == "coins":
                        if val == "0":
                            sprite = Coin(tile_size, x, y, gold_folder_path, val)
                        if val == "1":
                            sprite = Coin(tile_size, x, y, silver_folder_path, val)
                    if type == "enemies":
                        sprite = Enemy(tile_size, x, y)
                    if type == "constraints":
                        sprite = Tile(tile_size, x, y)
                    if sprite is not None:
                        sprite_group.add(sprite)
        return sprite_group

    def collision_enemy(self):
        """
        Gère la collision entre les ennemis et les contraintes.
        Inverse la direction des ennemis s'ils entrent en collision avec une contrainte.
        """
        for enemy in self.enemy_sprites.sprites():
            if pygame.sprite.spritecollide(enemy, self.constraint_sprites, False):
                enemy.reverse()

    def jump_particules(self, pos):
        """
        Ajoute des particules d'effet de saut à la position donnée.

        Args:
        pos (tuple): Position où les particules d'effet de saut doivent être créées.
        """
        jump_particule_sprite = ParticleEffect(pos, "jump")
        self.dust_sprite.add(jump_particule_sprite)

    def get_player_on_ground(self):
        """
        Vérifie si le joueur est sur le sol.
        Met à jour l'état du joueur en fonction de sa position par rapport au sol.
        """
        if self.player.sprite.terre:
            self.player_on_ground = True
        else:
            self.player_on_ground = False

    def create_landing_dust(self):
        """
        Gère la création d'effets de poussière lors de l'atterrissage du joueur.
        Crée des particules d'effet de poussière lorsque le joueur atterrit après un saut.
        """
        state = (
            not self.player_on_ground
            and self.player.sprite.terre
            and not self.dust_sprite.sprites()
        )
        if state:
            offset = pygame.math.Vector2(self.player.sprite.direction.x * -15, 25)
            fall_dust_particule = ParticleEffect(
                self.player.sprite.rect.midbottom - offset, "land"
            )
            self.dust_sprite.add(fall_dust_particule)

    def bordure_x(self):
        """
        Gère le déplacement horizontal du joueur en fonction de sa position sur l'écran.
        Ajuste la vitesse et le déplacement horizontal du joueur lorsque celui-ci atteint les bords de l'écran.
        """
        p = self.player.sprite
        if p.rect.centerx < 2 * screen_width / 4 and p.direction.x < 0:
            self.deplacement = self.vitesse_joueur
            p.v = 0
        elif p.rect.centerx > 2 * screen_width / 4 and p.direction.x > 0:
            self.deplacement = -self.vitesse_joueur
            p.v = 0
        else:
            self.deplacement = 0
            p.v = self.vitesse_joueur

    def collision_hori(self):
        """
        Gère la collision horizontale du joueur avec les tuiles du niveau.
        Vérifie et ajuste la position du joueur en fonction des collisions horizontales avec les tuiles.
        """
        p = self.player.sprite
        p.rect.x += p.direction.x * p.v
        collide = self.terrain_sprites.sprites()
        for sprite in collide:
            if sprite.rect.colliderect(p.rect):
                if p.direction.x < 0:
                    p.rect.left = sprite.rect.right
                elif p.direction.x > 0:
                    p.rect.right = sprite.rect.left

    def shoot(self):
        """
        Gère le tir des projectiles (tajines) par le joueur.
        Crée un nouveau projectile (tajine) lorsque le joueur tire et met à jour le cooldown du tir.
        """
        if self.tagine > 0:
            keys = pygame.key.get_pressed()
            p = self.player.sprite
            a = 0
            if keys[pygame.K_SPACE] and self.cooldown >= 100:
                if p.face == "right":
                    a = 1
                else:
                    a = -1
                self.tagine -= 1
                t = Tajine(p.rect.centerx, p.rect.centery, a)
                self.tajine_sprites.add(t)
                self.cooldown = 0

    def hit_enemy(self):
        """
        Gère les collisions entre le joueur et les ennemis.
        Vérifie les collisions et les interactions entre le joueur et les ennemis, comme le fait de tuer un ennemi,
        de perdre des points de vie ou de ralentir le joueur.
        """
        p = self.player.sprite
        p_bottom = p.rect.bottom
        enemy = self.enemy_sprites.sprites()
        enemy_collision = [e for e in enemy if e.rect.colliderect(p.rect)]
        if enemy_collision:
            for enemy in enemy_collision:
                e_center_y = enemy.rect.centery
                e_top = enemy.rect.top
                if e_top < p_bottom < e_center_y and p.direction.y > 0:
                    enemy.kill()
                    p.direction.y = -15
                    explosion_particule_sprite = ParticleEffect(
                        (p.rect.x, e_center_y), "explosion"
                    )
                    self.dust_sprite.add(explosion_particule_sprite)
                    self.score += 10
                    music("./music/Marioc_endie.wav", 1)
                else:
                    if not self.hit:
                        self.player_health -= 1
                        self.score -= 100
                        self.hit = True
                        self.fact = 0.25
                        self.vitesse_joueur = vitesse_joueur * self.fact
                        music("./music/Marioc_hit.wav", 0.3)
        if self.hit:
            self.count += 1
        if self.count >= 40:
            self.fact = 1
            self.vitesse_joueur = vitesse_joueur * self.fact
        if self.count >= 80:
            self.hit = False
            self.count = 0

    def hit_coin(self):
        """
        Gère la collecte des pièces par le joueur.
        Détecte les collisions entre le joueur et les pièces, et met à jour le score en fonction du type de pièce collectée.
        """
        p = self.player.sprite
        coins = self.coins_sprites.sprites()
        coins_collision = [c for c in coins if c.rect.colliderect(p.rect)]
        if coins_collision:
            for coin in coins_collision:
                if coin.rect.left < p.rect.centerx < coin.rect.right:
                    if coin.val == "0":
                        self.gold += 1
                        self.score += 20
                    elif coin.val == "1":
                        self.silver += 1
                        self.score += 5
                    coin.kill()
                    music("./music/Marioc_coin.wav", 0.1)

    def collision_tajine(self):
        """
        Gère les collisions entre les tajines (projectiles) et les tuiles ou les ennemis.
        Déclenche des actions en fonction des collisions des tajines avec les tuiles ou les ennemis,
        telles que la destruction des ennemis ou des effets spéciaux sur les tuiles.
        """
        for tajine in self.tajine_sprites:
            terrain_collision = [
                t for t in self.terrain_sprites if t.rect.colliderect(tajine.rect)
            ]
            enemy_coll = [
                t for t in self.enemy_sprites if t.rect.colliderect(tajine.rect)
            ]
            if len(terrain_collision) != 0:
                explosion_particule_sprite = ParticleEffect(
                    (tajine.rect.x, tajine.rect.y), "explosion"
                )
                self.dust_sprite.add(explosion_particule_sprite)
                music("./music/Marioc_tajine.wav", 0.1)
                tajine.kill()
            elif len(enemy_coll) != 0:
                for e in enemy_coll:
                    e.kill()
                    music("./music/Marioc_endie.wav", 1)
                    explosion_particule_sprite = ParticleEffect(
                        (tajine.rect.x, tajine.rect.y), "explosion"
                    )
                    self.dust_sprite.add(explosion_particule_sprite)
                    self.tagine += 1
                    self.score += 10
                tajine.kill()

    def collision_ver(self):
        """
        Gère la collision verticale du joueur avec les tuiles du niveau.
        Contrôle et ajuste la position verticale du joueur en fonction des collisions avec les tuiles.
        """
        p = self.player.sprite
        p.apply_gravity()
        collide = self.terrain_sprites.sprites()
        frappe = [sprite for sprite in collide if sprite.rect.colliderect(p.rect)]
        if p.direction.y > 0:
            for i in frappe[::-1]:
                p.rect.bottom = i.rect.top
                p.direction.y = 0
                p.terre = True
                break
        elif p.direction.y < 0:
            for i in frappe:
                p.rect.top = i.rect.bottom
                p.direction.y = 0
                p.terre = False
                break
        if len(frappe) == 0:
            p.terre = False
            if p.direction.y > p.gravity:
                p.status = "fall"

    def run(self):
        """
        Méthode principale pour exécuter le niveau de jeu.
        Gère l'ensemble du gameplay, y compris la mise à jour des éléments du niveau, des collisions,
        de la logique du joueur, des ennemis, des tirs, des particules et de la gestion du score.
        """
        # terrain
        self.terrain_sprites.draw(self.screen)
        self.terrain_sprites.update(self.deplacement)

        # enemy
        self.enemy_sprites.update(self.deplacement)
        self.constraint_sprites.update(self.deplacement)
        self.collision_enemy()
        self.enemy_sprites.draw(self.screen)
        self.hit_enemy()

        # coins
        self.coins_sprites.draw(self.screen)
        self.coins_sprites.update(self.deplacement)
        self.hit_coin()
        self.gui.show_coins((self.gold, self.silver))

        # stats
        self.gui.show_health(self.player_health)
        self.gui.show_tagine(self.tagine)
        self.gui.show_score(self.score)
        self.score = max(self.score, 0)

        # player
        self.player.update()
        self.collision_hori()
        self.collision_ver()
        self.create_landing_dust()
        self.get_player_on_ground()
        if not self.hit:
            self.player.draw(self.screen)
        else:
            if choice([True, False]):
                self.player.draw(self.screen)
        self.goal.update(self.deplacement)
        self.goal.draw(self.screen)

        # bug
        if self.hit:
            self.deplacement = 0
        self.bordure_x()
        self.death()
        # win
        self.win_situation()
        if self.win:
            self.score += self.player_health * 100
            music("./music/Marioc_win.wav", 0.2)

        # tajine
        self.shoot()
        self.collision_tajine()
        if self.cooldown < 105:
            self.cooldown += 1
        for tajine in self.tajine_sprites:
            tajine.go()
        self.tajine_sprites.update(self.deplacement)
        self.tajine_sprites.draw(self.screen)

        # dust
        self.dust_sprite.update(self.deplacement)
        self.dust_sprite.draw(self.screen)
        self.create_landing_dust()

        # changement score
        change_score(self.num, self.score)
