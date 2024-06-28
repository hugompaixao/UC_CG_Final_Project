import pygame
import random
import numpy as np
import math

from core.base import Base

from core_ext.camera import Camera
from core_ext.renderer import Renderer
from core_ext.scene import Scene

from objects_builders import *
from extras.movement_camera import MovementCamera
from extras.target_rig import TargetRig

from game_pages.gameCover import GameCover
from game_pages.instructions import Instructions
from game_pages.winning import Winning
from game_pages.gameOver import GameOver


from extras.movement_rig import MovementRig
from material.sprite import SpriteMaterial

# Delete
from extras.axes import AxesHelper
from extras.grid import GridHelper
#from extras.movement_rig import MovementRig
#from material.sprite import SpriteMaterial

class Game(Base):

    def initialize(self):
        print("Initializing Frisbee Coastal Quest...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspect_ratio=800/600)
        self.cameraRig = MovementCamera()
        self.rig = MovementRig()
        self.cameraRig.add(self.camera)
        #self.rig.add(self.camera) # to remove
        self.rig.add(self.cameraRig)
        #self.scene.add(self.rig)
        #self.rig.set_position([-600, 2, 4]) # to remove
        
        # Music 
    
        # Carregue as músicas
        self.music1 = pygame.mixer.Sound('sound/music/musicLoopDone2.mp3')
        self.music2 = pygame.mixer.Sound('sound/ocean/ocean.mp3')
        self.hitSound = pygame.mixer.Sound('sound/frisbeesound/glasshit2.mp3')
            

        # Defina o volume das músicas
        self.music1.set_volume(0.2)
        self.music2.set_volume(0.4)

        # Reproduza as músicas
        self.music1.play(loops=-1)
        self.music2.play(loops=-1)
        

        # Pages
        
        self.game_cover = GameCover()
        self.game_cover.set_position([1610, 0, -100])

        self.instructions = Instructions()
        self.instructions.set_position([1607.5, 0, -100])

        self.game_over = GameOver()
        self.game_over.set_position([1605, 0, -100])

        self.winning = Winning()
        self.winning.set_position([1602.5, 0, -100])
        

        # Fixed - Level / Wind / Trys / Strength
        # Level
        levels_geometry = RectangleGeometry(width = 0.5, height = 0.1)
        levels_texture = Texture("images/niveis.png")
        levels_sprite = SpriteMaterial(levels_texture, {
            "billboard" : 1, 
            "tileCount" : [1, 5],
            "tileNumber" : 0 
        })

        # Wind
        winds_geometry = RectangleGeometry(width = 0.15, height = 0.2)
        winds_texture = Texture("images/winds.png")
        winds_sprite = SpriteMaterial(winds_texture, {
            "billboard" : 1, 
            "tileCount" : [1, 2],
            "tileNumber" : 0 
        })

        # Frisbees
        n_frisbees_geometry = RectangleGeometry(width = 0.5, height = 0.125)
        n_frisbees_texture = Texture("images/frisbee5.png")
        n_frisbees_sprite = SpriteMaterial(n_frisbees_texture, {
            "billboard" : 1, 
            "tileCount" : [1, 4],
            "tileNumber" : 3 
        })

        # Strength Bar
        strength_bar_geometry = RectangleGeometry(width = 0.5, height = 0.125)
        strength_bar_texture = Texture("images/energy_bar.png")
        strength_bar_sprite = SpriteMaterial(strength_bar_texture, {
            "billboard" : 1, 
            "tileCount" : [1, 4],
            "tileNumber" : 0 
        })

        # Crosshair
        crosshair_geometry = RectangleGeometry(width = 1, height = 1.1)
        crosshair_texture = Texture("images/crosshair.png")
        crosshair_sprite = SpriteMaterial(crosshair_texture)
        
        # Build and Position
        self.frisbee = frisbee_builder()
        self.frisbee.rotate_x(-math.pi/2)
        self.frisbee.set_position([0,-0.3,-0.7])
        self.frisbee.scale(0.8)
        self.levels = Mesh(levels_geometry, levels_sprite)
        self.levels.set_position([0,0.55,-1])
        self.winds = Mesh(winds_geometry, winds_sprite)
        self.winds.set_position([0,0.40,-1])
        self.n_frisbees = Mesh(n_frisbees_geometry, n_frisbees_sprite)
        self.n_frisbees.set_position([0.55,-0.3,-1])
        self.strength_bar = Mesh(strength_bar_geometry, strength_bar_sprite)
        self.strength_bar.set_position([0.55,-0.45,-1])
        self.crosshair = Mesh(crosshair_geometry, crosshair_sprite)
        self.crosshair.set_position([0,0,-2])

        self.rig.add(self.frisbee)
        self.rig.add(self.levels)
        self.rig.add(self.winds)
        self.rig.add(self.n_frisbees)
        self.rig.add(self.strength_bar)
        self.rig.add(self.crosshair)

        self.rig.set_position([0, 2, 20])
        self.scene.add(self.rig)


        self.frisbees=[frisbee_builder(),
                       frisbee_builder(),
                       frisbee_builder()]
        self.frisbees[0].set_position([100,100,100])
        self.frisbees[1].set_position([100,100,100])
        self.frisbees[2].set_position([100,100,100])
        self.scene.add(self.frisbees[0])
        self.scene.add(self.frisbees[1])
        self.scene.add(self.frisbees[2])


        

         # LEVEL 1 - SCENARIO - DONE

        # Objects
        # Sky
        self.l1_sky = sky_builder()
        self.l1_sky.translate(0, 0, 0)

        # Floor
        self.l1_ground = ground_builder()
        self.l1_ground.rotate_x(-math.pi/2)
        self.l1_ground.translate(0, 0, 0)

        # Sea
        self.l1_sea = sea_builder()
        self.l1_sea.translate(0, 1, -70)

        # Palmtrees
        self.l1_palmtree_log_1 = log_builder()
        self.l1_palmtree_leafs_1 = leafs_builder()
        self.l1_palmtree_log_1.translate(0, 0, 60)
        self.l1_palmtree_leafs_1.translate(0, 0, 60)

        self.l1_palmtree_log_2 = log_builder()
        self.l1_palmtree_leafs_2 = leafs_builder()
        self.l1_palmtree_log_2.translate(10, 0, 50)
        self.l1_palmtree_leafs_2.translate(10, 0, 50)
        
        self.l1_palmtree_log_3 = log_builder()
        self.l1_palmtree_leafs_3 = leafs_builder()
        self.l1_palmtree_log_3.translate(20, 0, 70)
        self.l1_palmtree_leafs_3.translate(20, 0, 70)
        
        self.l1_palmtree_log_4 = log_builder()
        self.l1_palmtree_leafs_4 = leafs_builder()
        self.l1_palmtree_log_4.translate(30, 0, 60)
        self.l1_palmtree_leafs_4.translate(30, 0, 60)
        
        self.l1_palmtree_log_5 = log_builder()
        self.l1_palmtree_leafs_5 = leafs_builder()
        self.l1_palmtree_log_5.translate(35, 0, 50)
        self.l1_palmtree_leafs_5.translate(35, 0, 50)        

        self.l1_palmtree_log_6 = log_builder()
        self.l1_palmtree_leafs_6 = leafs_builder()
        self.l1_palmtree_log_6.translate(50, 0, 60)
        self.l1_palmtree_leafs_6.translate(50, 0, 60)        

        self.l1_palmtree_log_7 = log_builder()
        self.l1_palmtree_leafs_7 = leafs_builder()
        self.l1_palmtree_log_7.translate(-10, 0, 50)
        self.l1_palmtree_leafs_7.translate(-10, 0, 50)       

        self.l1_palmtree_log_8 = log_builder()
        self.l1_palmtree_leafs_8 = leafs_builder()
        self.l1_palmtree_log_8.translate(-20, 0, 60)
        self.l1_palmtree_leafs_8.translate(-20, 0, 60)
        
        self.l1_palmtree_log_9 = log_builder()
        self.l1_palmtree_leafs_9 = leafs_builder()
        self.l1_palmtree_log_9.translate(-25, 0, 50)
        self.l1_palmtree_leafs_9.translate(-25, 0, 50)
        
        self.l1_palmtree_log_10 = log_builder()
        self.l1_palmtree_leafs_10 = leafs_builder()
        self.l1_palmtree_log_10.translate(-35, 0, 60)
        self.l1_palmtree_leafs_10.translate(-35, 0, 60)       

        self.l1_palmtree_log_11 = log_builder()
        self.l1_palmtree_leafs_11 = leafs_builder()
        self.l1_palmtree_log_11.translate(-50, 0, 70)
        self.l1_palmtree_leafs_11.translate(-50, 0, 70)

        # Rocks
        # Big Rocks
        self.l1_rock_1 = big_rock_builder()
        self.l1_rock_1.translate(-50, 2, -45)
        self.l1_rock_2 = big_rock_builder()
        self.l1_rock_2.translate(-40, -2, -50)
        self.l1_rock_3 = big_rock_builder()
        self.l1_rock_3.translate(-60, 0, -60)

        # Small Rocks 
        self.l1_small_rock_1 = small_rock_builder()
        self.l1_small_rock_1.translate(-70, 0, -15)
        self.l1_small_rock_2 = small_rock_builder()
        self.l1_small_rock_2.translate(-30, 0, -25)
        self.l1_small_rock_3 = small_rock_builder()
        self.l1_small_rock_3.translate(-00, 0, 5)

        self.l1_small_rock_4 = small_rock_builder()
        self.l1_small_rock_4.translate(50, 0, 5)
        self.l1_small_rock_5 = small_rock_builder()
        self.l1_small_rock_5.translate(20, 0, 0)
        self.l1_small_rock_6 = small_rock_builder()
        self.l1_small_rock_6.translate(0, 0, 50)

        self.l1_small_rock_7 = small_rock_builder()
        self.l1_small_rock_7.translate(50, 0, 65)
        self.l1_small_rock_8 = small_rock_builder()
        self.l1_small_rock_8.translate(40, 0, 55)
        self.l1_small_rock_9 = small_rock_builder()
        self.l1_small_rock_9.translate(-90, 0, 50)

        # Seller
        self.l1_seller = person_up_builder()
        self.l1_seller.scale(0.6)
        self.l1_seller.translate(70, 0.45, -20)
        self.l1_cooler = cooler_builder()
        self.l1_cooler.scale(0.6)
        self.l1_cooler.translate(70, 0, -15)

        # Added to Scene
        self.scene.add(self.l1_sky)
        self.scene.add(self.l1_ground)
        self.scene.add(self.l1_sea)
        self.scene.add(self.l1_palmtree_log_1)
        self.scene.add(self.l1_palmtree_leafs_1)
        self.scene.add(self.l1_palmtree_log_2)
        self.scene.add(self.l1_palmtree_leafs_2)
        self.scene.add(self.l1_palmtree_log_3)
        self.scene.add(self.l1_palmtree_leafs_3)
        self.scene.add(self.l1_palmtree_log_4)
        self.scene.add(self.l1_palmtree_leafs_4)
        self.scene.add(self.l1_palmtree_log_5)
        self.scene.add(self.l1_palmtree_leafs_5)
        self.scene.add(self.l1_palmtree_log_6)
        self.scene.add(self.l1_palmtree_leafs_6)
        self.scene.add(self.l1_palmtree_log_7)
        self.scene.add(self.l1_palmtree_leafs_7)
        self.scene.add(self.l1_palmtree_log_8)
        self.scene.add(self.l1_palmtree_leafs_8)
        self.scene.add(self.l1_palmtree_log_9)
        self.scene.add(self.l1_palmtree_leafs_9)
        self.scene.add(self.l1_palmtree_log_10)
        self.scene.add(self.l1_palmtree_leafs_10)
        self.scene.add(self.l1_palmtree_log_11)
        self.scene.add(self.l1_palmtree_leafs_11)
        self.scene.add(self.l1_rock_1)
        self.scene.add(self.l1_rock_2)
        self.scene.add(self.l1_rock_3)
        self.scene.add(self.l1_small_rock_1)
        self.scene.add(self.l1_small_rock_2)
        self.scene.add(self.l1_small_rock_3)
        self.scene.add(self.l1_small_rock_4)
        self.scene.add(self.l1_small_rock_5)
        self.scene.add(self.l1_small_rock_6)
        self.scene.add(self.l1_small_rock_7)
        self.scene.add(self.l1_small_rock_8)
        self.scene.add(self.l1_small_rock_9)
        self.scene.add(self.l1_small_rock_1)
        self.scene.add(self.l1_small_rock_2)
        self.scene.add(self.l1_small_rock_3)
        self.scene.add(self.l1_small_rock_4)
        self.scene.add(self.l1_small_rock_5)
        self.scene.add(self.l1_small_rock_6)
        self.scene.add(self.l1_small_rock_7)
        self.scene.add(self.l1_small_rock_8)
        self.scene.add(self.l1_small_rock_9)
        self.scene.add(self.l1_seller)
        self.scene.add(self.l1_cooler)
        
        # LEVEL 2 - SCENARIO - DONE
        
        # Objects
        # Sky
        self.l2_sky = sky_builder()
        self.l2_sky.translate(900, 0, 0)
        self.scene.add(self.l2_sky)

        # Floor
        self.l2_ground = ground_builder()
        self.l2_ground.rotate_x(-math.pi/2)
        self.l2_ground.translate(900, 0, 0)
        self.scene.add(self.l2_ground)

        # Sea
        self.l2_sea = sea_builder()
        self.l2_sea.translate(900, 1, -70)

        # Palmtrees
        self.l2_palmtree_log_1 = log_builder()
        self.l2_palmtree_leafs_1 = leafs_builder()
        self.l2_palmtree_log_1.translate(900, 0, 60)
        self.l2_palmtree_leafs_1.translate(900, 0, 60)

        self.l2_palmtree_log_2 = log_builder()
        self.l2_palmtree_leafs_2 = leafs_builder()
        self.l2_palmtree_log_2.translate(910, 0, 50)
        self.l2_palmtree_leafs_2.translate(910, 0, 50)
        
        self.l2_palmtree_log_3 = log_builder()
        self.l2_palmtree_leafs_3 = leafs_builder()
        self.l2_palmtree_log_3.translate(920, 0, 70)
        self.l2_palmtree_leafs_3.translate(920, 0, 70)
        
        self.l2_palmtree_log_4 = log_builder()
        self.l2_palmtree_leafs_4 = leafs_builder()
        self.l2_palmtree_log_4.translate(930, 0, 60)
        self.l2_palmtree_leafs_4.translate(930, 0, 60)
        
        self.l2_palmtree_log_5 = log_builder()
        self.l2_palmtree_leafs_5 = leafs_builder()
        self.l2_palmtree_log_5.translate(935, 0, 50)
        self.l2_palmtree_leafs_5.translate(935, 0, 50)        

        self.l2_palmtree_log_6 = log_builder()
        self.l2_palmtree_leafs_6 = leafs_builder()
        self.l2_palmtree_log_6.translate(950, 0, 60)
        self.l2_palmtree_leafs_6.translate(950, 0, 60)        

        self.l2_palmtree_log_7 = log_builder()
        self.l2_palmtree_leafs_7 = leafs_builder()
        self.l2_palmtree_log_7.translate(890, 0, 50)
        self.l2_palmtree_leafs_7.translate(890, 0, 50)       

        self.l2_palmtree_log_8 = log_builder()
        self.l2_palmtree_leafs_8 = leafs_builder()
        self.l2_palmtree_log_8.translate(880, 0, 60)
        self.l2_palmtree_leafs_8.translate(880, 0, 60)
        
        self.l2_palmtree_log_9 = log_builder()
        self.l2_palmtree_leafs_9 = leafs_builder()
        self.l2_palmtree_log_9.translate(875, 0, 50)
        self.l2_palmtree_leafs_9.translate(875, 0, 50)
        
        self.l2_palmtree_log_10 = log_builder()
        self.l2_palmtree_leafs_10 = leafs_builder()
        self.l2_palmtree_log_10.translate(865, 0, 60)
        self.l2_palmtree_leafs_10.translate(865, 0, 60)       

        self.l2_palmtree_log_11 = log_builder()
        self.l2_palmtree_leafs_11 = leafs_builder()
        self.l2_palmtree_log_11.translate(850, 0, 70)
        self.l2_palmtree_leafs_11.translate(850, 0, 70)

        # Rocks
        # Big See Rocks
        self.l2_big_rock_1 = big_rock_builder()
        self.l2_big_rock_1.translate(850, 2, -45)
        self.l2_big_rock_2 = big_rock_builder()
        self.l2_big_rock_2.translate(860, -2, -50)
        self.l2_big_rock_3 = big_rock_builder()
        self.l2_big_rock_3.translate(940, 0, -60)

        # Small Rocks 
        self.l2_small_rock_1 = small_rock_builder()
        self.l2_small_rock_1.translate(830, 0, -15)
        self.l2_small_rock_2 = small_rock_builder()
        self.l2_small_rock_2.translate(870, 0, -25)
        self.l2_small_rock_3 = small_rock_builder()
        self.l2_small_rock_3.translate(903, 0.2, -23)

        self.l2_small_rock_4 = small_rock_builder()
        self.l2_small_rock_4.translate(950, 0, 5)
        self.l2_small_rock_5 = small_rock_builder()
        self.l2_small_rock_5.translate(920, 0, 0)
        self.l2_small_rock_6 = small_rock_builder()
        self.l2_small_rock_6.translate(900, 0, 50)

        self.l2_small_rock_7 = small_rock_builder()
        self.l2_small_rock_7.translate(950, 0, 65)
        self.l2_small_rock_8 = small_rock_builder()
        self.l2_small_rock_8.translate(960, 0, 55)
        self.l2_small_rock_9 = small_rock_builder()
        self.l2_small_rock_9.translate(810, 0, 50)

        # Seller 
        self.l2_seller = person_up_builder()
        self.l2_seller.scale(0.6)
        self.l2_seller.translate(1600, 0.45, -20)
        self.l2_cooler = cooler_builder()
        self.l2_cooler.scale(0.6)
        self.l2_cooler.translate(1600, 0, -15)
        
        # Beach Umbrelas
        self.l2_beach_umbrela_pole_1 = beach_umbrela_pole_builder()
        self.l2_beach_umbrela_1 = beach_umbrela_builder()
        self.l2_beach_umbrela_pole_1.translate(870, 0, -10)
        self.l2_beach_umbrela_1.translate(870, 0, -10)

        self.l2_beach_umbrela_pole_2 = beach_umbrela_pole_builder()
        self.l2_beach_umbrela_2 = beach_umbrela_builder()
        self.l2_beach_umbrela_pole_2.translate(880, 0, -20)
        self.l2_beach_umbrela_2.translate(880, 0, -20)

        self.l2_beach_umbrela_pole_3 = beach_umbrela_pole_builder()
        self.l2_beach_umbrela_3 = beach_umbrela_builder()
        self.l2_beach_umbrela_pole_3.translate(895, 0, -15)
        self.l2_beach_umbrela_3.translate(895, 0, -15)
    
        self.l2_beach_umbrela_pole_4 = beach_umbrela_pole_builder()
        self.l2_beach_umbrela_4 = beach_umbrela_builder()
        self.l2_beach_umbrela_pole_4.translate(905, 0, -20)
        self.l2_beach_umbrela_4.translate(905, 0, -20)

        self.l2_beach_umbrela_pole_5 = beach_umbrela_pole_builder()
        self.l2_beach_umbrela_5 = beach_umbrela_builder()
        self.l2_beach_umbrela_pole_5.translate(915, 0, -10)
        self.l2_beach_umbrela_5.translate(915, 0, -10)

        self.l2_beach_umbrela_pole_6 = beach_umbrela_pole_builder()
        self.l2_beach_umbrela_6 = beach_umbrela_builder()
        self.l2_beach_umbrela_pole_6.translate(935, 0, -15)
        self.l2_beach_umbrela_6.translate(935, 0, -15)

        # Added to Scene
        self.scene.add(self.l2_sky)
        self.scene.add(self.l2_ground)
        self.scene.add(self.l2_sea)
        self.scene.add(self.l2_palmtree_log_1)
        self.scene.add(self.l2_palmtree_leafs_1)
        self.scene.add(self.l2_palmtree_log_2)
        self.scene.add(self.l2_palmtree_leafs_2)
        self.scene.add(self.l2_palmtree_log_3)
        self.scene.add(self.l2_palmtree_leafs_3)
        self.scene.add(self.l2_palmtree_log_4)
        self.scene.add(self.l2_palmtree_leafs_4)
        self.scene.add(self.l2_palmtree_log_5)
        self.scene.add(self.l2_palmtree_leafs_5)
        self.scene.add(self.l2_palmtree_log_6)
        self.scene.add(self.l2_palmtree_leafs_6)
        self.scene.add(self.l2_palmtree_log_7)
        self.scene.add(self.l2_palmtree_leafs_7)
        self.scene.add(self.l2_palmtree_log_8)
        self.scene.add(self.l2_palmtree_leafs_8)
        self.scene.add(self.l2_palmtree_log_9)
        self.scene.add(self.l2_palmtree_leafs_9)
        self.scene.add(self.l2_palmtree_log_10)
        self.scene.add(self.l2_palmtree_leafs_10)
        self.scene.add(self.l2_palmtree_log_11)
        self.scene.add(self.l2_palmtree_leafs_11)
        self.scene.add(self.l2_big_rock_1)
        self.scene.add(self.l2_big_rock_2)
        self.scene.add(self.l2_big_rock_3)
        self.scene.add(self.l2_small_rock_1)
        self.scene.add(self.l2_small_rock_2)
        self.scene.add(self.l2_small_rock_3)
        self.scene.add(self.l2_small_rock_4)
        self.scene.add(self.l2_small_rock_5)
        self.scene.add(self.l2_small_rock_6)
        self.scene.add(self.l2_small_rock_7)
        self.scene.add(self.l2_small_rock_8)
        self.scene.add(self.l2_small_rock_9)
        self.scene.add(self.l2_seller)
        self.scene.add(self.l2_cooler)
        self.scene.add(self.l2_beach_umbrela_pole_1)
        self.scene.add(self.l2_beach_umbrela_1)
        self.scene.add(self.l2_beach_umbrela_pole_2)
        self.scene.add(self.l2_beach_umbrela_2)
        self.scene.add(self.l2_beach_umbrela_pole_3)
        self.scene.add(self.l2_beach_umbrela_3)
        self.scene.add(self.l2_beach_umbrela_pole_4)
        self.scene.add(self.l2_beach_umbrela_4)
        self.scene.add(self.l2_beach_umbrela_pole_5)
        self.scene.add(self.l2_beach_umbrela_5)
        self.scene.add(self.l2_beach_umbrela_pole_6)
        self.scene.add(self.l2_beach_umbrela_6)

        # LEVEL 3 - SCENARIO
        
        # Bandeira
        self.l3_poste = flag_pole_builder()
        self.l3_bandeira = flag_builder()
        self.l3_poste.translate(620, 0.3, 1)
        self.l3_bandeira.translate(620, 0.3, 1)

        # Sky
        self.l3_sky = sky_builder()
        self.l3_sky.translate(600, 0, 0)
        self.scene.add(self.l3_sky)

        # Sand
        self.l3_ground = ground_builder()
        self.l3_ground.rotate_x(-math.pi/2)
        self.l3_ground.translate(600, 0, 0)
        self.scene.add(self.l3_ground)

        # Sea
        self.l3_sea = sea_builder()
        self.l3_sea.translate(600, 1, -70)

        # Palmtrees
        self.l3_palmtree_log_1 = log_builder()
        self.l3_palmtree_leafs_1 = leafs_builder()
        self.l3_palmtree_log_1.translate(600, 0, 60)
        self.l3_palmtree_leafs_1.translate(600, 0, 60)

        self.l3_palmtree_log_2 = log_builder()
        self.l3_palmtree_leafs_2 = leafs_builder()
        self.l3_palmtree_log_2.translate(610, 0, 50)
        self.l3_palmtree_leafs_2.translate(610, 0, 50)
        
        self.l3_palmtree_log_3 = log_builder()
        self.l3_palmtree_leafs_3 = leafs_builder()
        self.l3_palmtree_log_3.translate(620, 0, 70)
        self.l3_palmtree_leafs_3.translate(620, 0, 70)
        
        self.l3_palmtree_log_4 = log_builder()
        self.l3_palmtree_leafs_4 = leafs_builder()
        self.l3_palmtree_log_4.translate(630, 0, 60)
        self.l3_palmtree_leafs_4.translate(630, 0, 60)
        
        self.l3_palmtree_log_5 = log_builder()
        self.l3_palmtree_leafs_5 = leafs_builder()
        self.l3_palmtree_log_5.translate(635, 0, 50)
        self.l3_palmtree_leafs_5.translate(635, 0, 50)        

        self.l3_palmtree_log_6 = log_builder()
        self.l3_palmtree_leafs_6 = leafs_builder()
        self.l3_palmtree_log_6.translate(650, 0, 60)
        self.l3_palmtree_leafs_6.translate(650, 0, 60)        

        self.l3_palmtree_log_7 = log_builder()
        self.l3_palmtree_leafs_7 = leafs_builder()
        self.l3_palmtree_log_7.translate(590, 0, 50)
        self.l3_palmtree_leafs_7.translate(590, 0, 50)       

        self.l3_palmtree_log_8 = log_builder()
        self.l3_palmtree_leafs_8 = leafs_builder()
        self.l3_palmtree_log_8.translate(580, 0, 60)
        self.l3_palmtree_leafs_8.translate(580, 0, 60)
        
        self.l3_palmtree_log_9 = log_builder()
        self.l3_palmtree_leafs_9 = leafs_builder()
        self.l3_palmtree_log_9.translate(575, 0, 50)
        self.l3_palmtree_leafs_9.translate(575, 0, 50)
        
        self.l3_palmtree_log_10 = log_builder()
        self.l3_palmtree_leafs_10 = leafs_builder()
        self.l3_palmtree_log_10.translate(565, 0, 60)
        self.l3_palmtree_leafs_10.translate(565, 0, 60)       

        self.l3_palmtree_log_11 = log_builder()
        self.l3_palmtree_leafs_11 = leafs_builder()
        self.l3_palmtree_log_11.translate(550, 0, 70)
        self.l3_palmtree_leafs_11.translate(550, 0, 70)

        # Rocks
        self.l3_rock_1 = big_rock_builder()
        self.l3_rock_1.translate(550, 2, -45)
        self.l3_rock_2 = big_rock_builder()
        self.l3_rock_2.translate(560, -2, -50)
        self.l3_rock_3 = big_rock_builder()
        self.l3_rock_3.translate(640, 0, -60)

        # Small Rocks 
        self.l3_small_rock_1 = small_rock_builder()
        self.l3_small_rock_1.translate(530, 0, -15)
        self.l3_small_rock_2 = small_rock_builder()
        self.l3_small_rock_2.translate(570, 0, -25)
        self.l3_small_rock_3 = small_rock_builder()
        self.l3_small_rock_3.translate(598, 0.2, -8)

        self.l3_small_rock_4 = small_rock_builder()
        self.l3_small_rock_4.translate(550, 0, 5)
        self.l3_small_rock_5 = small_rock_builder()
        self.l3_small_rock_5.translate(580, 0, 0)
        self.l3_small_rock_6 = small_rock_builder()
        self.l3_small_rock_6.translate(600, 0, 50)

        self.l3_small_rock_7 = small_rock_builder()
        self.l3_small_rock_7.translate(550, 0, 65)
        self.l3_small_rock_8 = small_rock_builder()
        self.l3_small_rock_8.translate(560, 0, 55)
        self.l3_small_rock_9 = small_rock_builder()
        self.l3_small_rock_9.translate(510, 0, 50)

        # Seller
        self.l3_seller = person_up_builder()
        self.l3_seller.scale(0.6)
        self.l3_seller.translate(1130, 0.45, -20)
        self.l3_cooler = cooler_builder()
        self.l3_cooler.scale(0.6)
        self.l3_cooler.translate(1130, 0, -15)

        # Beach Umbrelas
        self.l3_beach_umbrela_pole_1 = beach_umbrela_pole_builder()
        self.l3_beach_umbrela_1 = beach_umbrela_builder()
        self.l3_beach_umbrela_pole_1.translate(570, 0, -10)
        self.l3_beach_umbrela_1.translate(570, 0, -10)

        self.l3_beach_umbrela_pole_2 = beach_umbrela_pole_builder()
        self.l3_beach_umbrela_2 = beach_umbrela_builder()
        self.l3_beach_umbrela_pole_2.translate(580, 0, -20)
        self.l3_beach_umbrela_2.translate(580, 0, -20)

        self.l3_beach_umbrela_pole_3 = beach_umbrela_pole_builder()
        self.l3_beach_umbrela_3 = beach_umbrela_builder()
        self.l3_beach_umbrela_pole_3.translate(595, 0, -15)
        self.l3_beach_umbrela_3.translate(595, 0, -15)
    
        self.l3_beach_umbrela_pole_4 = beach_umbrela_pole_builder()
        self.l3_beach_umbrela_4 = beach_umbrela_builder()
        self.l3_beach_umbrela_pole_4.translate(605, 0, -20)
        self.l3_beach_umbrela_4.translate(605, 0, -20)

        self.l3_beach_umbrela_pole_5 = beach_umbrela_pole_builder()
        self.l3_beach_umbrela_5 = beach_umbrela_builder()
        self.l3_beach_umbrela_pole_5.translate(615, 0, -10)
        self.l3_beach_umbrela_5.translate(615, 0, -10)

        self.l3_beach_umbrela_pole_6 = beach_umbrela_pole_builder()
        self.l3_beach_umbrela_6 = beach_umbrela_builder()
        self.l3_beach_umbrela_pole_6.translate(635, 0, -15)
        self.l3_beach_umbrela_6.translate(635, 0, -15)

        # Buoy
        self.l3_buoy_1 = buoy_builder()
        self.l3_buoy_1.translate(565, 1.5, -45)
        self.l3_buoy_2 = buoy_builder()
        self.l3_buoy_2.translate(590, 1.25, -40)
        self.l3_buoy_3 = buoy_builder()
        self.l3_buoy_3.translate(600, 1.25, -30)
        self.l3_buoy_4 = buoy_builder()
        self.l3_buoy_4.translate(615, 1.25, -35)
        

        # Added to Scene
        self.scene.add(self.l3_poste)
        self.scene.add(self.l3_bandeira)
        self.scene.add(self.l3_sky)
        self.scene.add(self.l3_ground)
        self.scene.add(self.l3_sea)
        self.scene.add(self.l3_palmtree_log_1)
        self.scene.add(self.l3_palmtree_leafs_1)
        self.scene.add(self.l3_palmtree_log_2)
        self.scene.add(self.l3_palmtree_leafs_2)
        self.scene.add(self.l3_palmtree_log_3)
        self.scene.add(self.l3_palmtree_leafs_3)
        self.scene.add(self.l3_palmtree_log_4)
        self.scene.add(self.l3_palmtree_leafs_4)
        self.scene.add(self.l3_palmtree_log_5)
        self.scene.add(self.l3_palmtree_leafs_5)
        self.scene.add(self.l3_palmtree_log_6)
        self.scene.add(self.l3_palmtree_leafs_6)
        self.scene.add(self.l3_palmtree_log_7)
        self.scene.add(self.l3_palmtree_leafs_7)
        self.scene.add(self.l3_palmtree_log_8)
        self.scene.add(self.l3_palmtree_leafs_8)
        self.scene.add(self.l3_palmtree_log_9)
        self.scene.add(self.l3_palmtree_leafs_9)
        self.scene.add(self.l3_palmtree_log_10)
        self.scene.add(self.l3_palmtree_leafs_10)
        self.scene.add(self.l3_palmtree_log_11)
        self.scene.add(self.l3_palmtree_leafs_11)
        self.scene.add(self.l3_rock_1)
        self.scene.add(self.l3_rock_2)
        self.scene.add(self.l3_rock_3)
        self.scene.add(self.l3_small_rock_1)
        self.scene.add(self.l3_small_rock_2)
        self.scene.add(self.l3_small_rock_3)
        self.scene.add(self.l3_small_rock_4)
        self.scene.add(self.l3_small_rock_5)
        self.scene.add(self.l3_small_rock_6)
        self.scene.add(self.l3_small_rock_7)
        self.scene.add(self.l3_small_rock_8)
        self.scene.add(self.l3_small_rock_9)
        self.scene.add(self.l3_seller)
        self.scene.add(self.l3_cooler)
        self.scene.add(self.l3_beach_umbrela_pole_1)
        self.scene.add(self.l3_beach_umbrela_1)
        self.scene.add(self.l3_beach_umbrela_pole_2)
        self.scene.add(self.l3_beach_umbrela_2)
        self.scene.add(self.l3_beach_umbrela_pole_3)
        self.scene.add(self.l3_beach_umbrela_3)
        self.scene.add(self.l3_beach_umbrela_pole_4)
        self.scene.add(self.l3_beach_umbrela_4)
        self.scene.add(self.l3_beach_umbrela_pole_5)
        self.scene.add(self.l3_beach_umbrela_5)
        self.scene.add(self.l3_beach_umbrela_pole_6)
        self.scene.add(self.l3_beach_umbrela_6)
        self.scene.add(self.l3_buoy_1)
        self.scene.add(self.l3_buoy_2)
        self.scene.add(self.l3_buoy_3)
        self.scene.add(self.l3_buoy_4)
        # LEVEL 4 - SCENARIO
        
        # Objects
        # Bandeira
        self.l4_poste = flag_pole_builder()
        self.l4_bandeira = flag_builder()
        self.l4_poste.translate(330, 0.3, -1)
        self.l4_bandeira.translate(330, 0.3, -1)

        # Sky
        self.l4_sky = sky_builder()
        self.l4_sky.translate(300, 0, 0)
        self.scene.add(self.l4_sky)

        # Floor
        self.l4_ground = ground_builder()
        self.l4_ground.rotate_x(-math.pi/2)
        self.l4_ground.translate(300, 0, 0)
        self.scene.add(self.l4_ground)

        # Sea
        self.l4_sea = sea_builder()
        self.l4_sea.translate(300, 1, -70)

        # Palmtrees
        self.l4_palmtree_log_1 = log_builder()
        self.l4_palmtree_leafs_1 = leafs_builder()
        self.l4_palmtree_log_1.translate(300, 0, 60)
        self.l4_palmtree_leafs_1.translate(300, 0, 60)

        self.l4_palmtree_log_2 = log_builder()
        self.l4_palmtree_leafs_2 = leafs_builder()
        self.l4_palmtree_log_2.translate(310, 0, 50)
        self.l4_palmtree_leafs_2.translate(310, 0, 50)
        
        self.l4_palmtree_log_3 = log_builder()
        self.l4_palmtree_leafs_3 = leafs_builder()
        self.l4_palmtree_log_3.translate(320, 0, 70)
        self.l4_palmtree_leafs_3.translate(320, 0, 70)
        
        self.l4_palmtree_log_4 = log_builder()
        self.l4_palmtree_leafs_4 = leafs_builder()
        self.l4_palmtree_log_4.translate(330, 0, 60)
        self.l4_palmtree_leafs_4.translate(330, 0, 60)
        
        self.l4_palmtree_log_5 = log_builder()
        self.l4_palmtree_leafs_5 = leafs_builder()
        self.l4_palmtree_log_5.translate(335, 0, 50)
        self.l4_palmtree_leafs_5.translate(335, 0, 50)        

        self.l4_palmtree_log_6 = log_builder()
        self.l4_palmtree_leafs_6 = leafs_builder()
        self.l4_palmtree_log_6.translate(350, 0, 48)
        self.l4_palmtree_leafs_6.translate(350, 0, 48)        

        self.l4_palmtree_log_7 = log_builder()
        self.l4_palmtree_leafs_7 = leafs_builder()
        self.l4_palmtree_log_7.translate(290, 0, 50)
        self.l4_palmtree_leafs_7.translate(290, 0, 50)       

        self.l4_palmtree_log_8 = log_builder()
        self.l4_palmtree_leafs_8 = leafs_builder()
        self.l4_palmtree_log_8.translate(280, 0, 60)
        self.l4_palmtree_leafs_8.translate(280, 0, 60)
        
        self.l4_palmtree_log_9 = log_builder()
        self.l4_palmtree_leafs_9 = leafs_builder()
        self.l4_palmtree_log_9.translate(275, 0, 50)
        self.l4_palmtree_leafs_9.translate(275, 0, 50)
        
        self.l4_palmtree_log_10 = log_builder()
        self.l4_palmtree_leafs_10 = leafs_builder()
        self.l4_palmtree_log_10.translate(265, 0, 60)
        self.l4_palmtree_leafs_10.translate(265, 0, 60)       

        self.l4_palmtree_log_11 = log_builder()
        self.l4_palmtree_leafs_11 = leafs_builder()
        self.l4_palmtree_log_11.translate(250, 0, 70)
        self.l4_palmtree_leafs_11.translate(250, 0, 70)

        # Rocks
        self.l4_rock_1 = big_rock_builder()
        self.l4_rock_1.translate(250, 2, -45)
        self.l4_rock_2 = big_rock_builder()
        self.l4_rock_2.translate(260, -2, -50)
        self.l4_rock_3 = big_rock_builder()
        self.l4_rock_3.translate(340, 0, -60)

        # Small Rocks 
        self.l4_small_rock_1 = small_rock_builder()
        self.l4_small_rock_1.translate(270, 0, -15)
        self.l4_small_rock_2 = small_rock_builder()
        self.l4_small_rock_2.translate(230, 0, -25)
        self.l4_small_rock_3 = small_rock_builder()
        self.l4_small_rock_3.translate(300, 0, -10)

        self.l4_small_rock_4 = small_rock_builder()
        self.l4_small_rock_4.translate(350, 0, 5)
        self.l4_small_rock_5 = small_rock_builder()
        self.l4_small_rock_5.translate(320, 0, 0)
        self.l4_small_rock_6 = small_rock_builder()
        self.l4_small_rock_6.translate(300, 0, 50)

        self.l4_small_rock_7 = small_rock_builder()
        self.l4_small_rock_7.translate(350, 0, 65)
        self.l4_small_rock_8 = small_rock_builder()
        self.l4_small_rock_8.translate(340, 0, 55)
        self.l4_small_rock_9 = small_rock_builder()
        self.l4_small_rock_9.translate(290, 0, 50)

        # Seller
        self.l4_seller = person_up_builder()
        self.l4_seller.scale(0.6)
        self.l4_seller.translate(570, 0.45, -20)
        self.l4_cooler = cooler_builder()
        self.l4_cooler.scale(0.6)
        self.l4_cooler.translate(570, 0, -15)

        # Beach Umbrelas
        self.l4_beach_umbrela_pole_1 = beach_umbrela_pole_builder()
        self.l4_beach_umbrela_1 = beach_umbrela_builder()
        self.l4_beach_umbrela_pole_1.translate(270, 0, -10)
        self.l4_beach_umbrela_1.translate(270, 0, -10)

        self.l4_beach_umbrela_pole_2 = beach_umbrela_pole_builder()
        self.l4_beach_umbrela_2 = beach_umbrela_builder()
        self.l4_beach_umbrela_pole_2.translate(280, 0, -20)
        self.l4_beach_umbrela_2.translate(280, 0, -20)

        self.l4_beach_umbrela_pole_3 = beach_umbrela_pole_builder()
        self.l4_beach_umbrela_3 = beach_umbrela_builder()
        self.l4_beach_umbrela_pole_3.translate(295, 0, -15)
        self.l4_beach_umbrela_3.translate(295, 0, -15)
    
        self.l4_beach_umbrela_pole_4 = beach_umbrela_pole_builder()
        self.l4_beach_umbrela_4 = beach_umbrela_builder()
        self.l4_beach_umbrela_pole_4.translate(305, 0, -20)
        self.l4_beach_umbrela_4.translate(305, 0, -20)

        self.l4_beach_umbrela_pole_5 = beach_umbrela_pole_builder()
        self.l4_beach_umbrela_5 = beach_umbrela_builder()
        self.l4_beach_umbrela_pole_5.translate(315, 0, -10)
        self.l4_beach_umbrela_5.translate(315, 0, -10)

        self.l4_beach_umbrela_pole_6 = beach_umbrela_pole_builder()
        self.l4_beach_umbrela_6 = beach_umbrela_builder()
        self.l4_beach_umbrela_pole_6.translate(335, 0, -15)
        self.l4_beach_umbrela_6.translate(335, 0, -15)

         # Buoy
        self.l4_buoy_1 = buoy_builder()
        self.l4_buoy_1.translate(265, 1.5, -45)
        self.l4_buoy_2 = buoy_builder()
        self.l4_buoy_2.translate(290, 1.25, -40)
        self.l4_buoy_3 = buoy_builder()
        self.l4_buoy_3.translate(300, 1.25, -35)
        self.l4_buoy_4 = buoy_builder()
        self.l4_buoy_4.translate(315, 1.25, -35)
        self.l4_buoy_5 = buoy_builder()
        self.l4_buoy_5.translate(312, 0.3, 3)
        
        # People Under Beach Umbrellas
        self.beach_umbrella_person_1 = person_down_builder()
        self.beach_umbrella_person_1.scale(0.6)
        self.beach_umbrella_person_1.translate(451.5, 0, -16.25)

        self.beach_umbrella_person_2 = person_down_builder()
        self.beach_umbrella_person_2.scale(0.6)
        self.beach_umbrella_person_2.translate(464.5, 0, -31.5)

        self.beach_umbrella_person_3 = person_down_builder()
        self.beach_umbrella_person_3.scale(0.6)
        self.beach_umbrella_person_3.translate(493.5, 0, -25.5)

        self.beach_umbrella_person_4 = person_down_builder()
        self.beach_umbrella_person_4.scale(0.6)
        self.beach_umbrella_person_4.translate(507, 0, -31)

        self.beach_umbrella_person_5 = person_down_builder()
        self.beach_umbrella_person_5.scale(0.6)
        self.beach_umbrella_person_5.translate(527.5, 0, -16)

        self.beach_umbrella_person_6 = person_down_builder()
        self.beach_umbrella_person_6.scale(0.6)
        self.beach_umbrella_person_6.translate(557, 0, -25)

        # People in Buoys
        self.buoy_person_1 = person_up_builder()
        self.buoy_person_1.scale(0.6)
        self.buoy_person_1.translate(442, -1.5, -73.75)

        self.buoy_person_2 = person_up_builder()
        self.buoy_person_2.scale(0.6)
        self.buoy_person_2.translate(483.25, -1.5, -65.75)

        self.buoy_person_3 = person_up_builder()
        self.buoy_person_3.scale(0.6)
        self.buoy_person_3.translate(500, -1.5, -58.25)
        
        self.buoy_person_4 = person_up_builder()
        self.buoy_person_4.scale(0.6)
        self.buoy_person_4.translate(525.25, -1.5, -58.5)
        

        # Added to Scene
        self.scene.add(self.l4_poste)
        self.scene.add(self.l4_bandeira)
        self.scene.add(self.l4_sky)
        self.scene.add(self.l4_ground)
        self.scene.add(self.l4_sea)
        self.scene.add(self.l4_palmtree_log_1)
        self.scene.add(self.l4_palmtree_leafs_1)
        self.scene.add(self.l4_palmtree_log_2)
        self.scene.add(self.l4_palmtree_leafs_2)
        self.scene.add(self.l4_palmtree_log_3)
        self.scene.add(self.l4_palmtree_leafs_3)
        self.scene.add(self.l4_palmtree_log_4)
        self.scene.add(self.l4_palmtree_leafs_4)
        self.scene.add(self.l4_palmtree_log_5)
        self.scene.add(self.l4_palmtree_leafs_5)
        self.scene.add(self.l4_palmtree_log_6)
        self.scene.add(self.l4_palmtree_leafs_6)
        self.scene.add(self.l4_palmtree_log_7)
        self.scene.add(self.l4_palmtree_leafs_7)
        self.scene.add(self.l4_palmtree_log_8)
        self.scene.add(self.l4_palmtree_leafs_8)
        self.scene.add(self.l4_palmtree_log_9)
        self.scene.add(self.l4_palmtree_leafs_9)
        self.scene.add(self.l4_palmtree_log_10)
        self.scene.add(self.l4_palmtree_leafs_10)
        self.scene.add(self.l4_palmtree_log_11)
        self.scene.add(self.l4_palmtree_leafs_11)
        self.scene.add(self.l4_rock_1)
        self.scene.add(self.l4_rock_2)
        self.scene.add(self.l4_rock_3)
        self.scene.add(self.l4_small_rock_1)
        self.scene.add(self.l4_small_rock_2)
        self.scene.add(self.l4_small_rock_3)
        self.scene.add(self.l4_small_rock_4)
        self.scene.add(self.l4_small_rock_5)
        self.scene.add(self.l4_small_rock_6)
        self.scene.add(self.l4_small_rock_7)
        self.scene.add(self.l4_small_rock_8)
        self.scene.add(self.l4_small_rock_9)
        self.scene.add(self.l4_seller)
        self.scene.add(self.l4_cooler)
        self.scene.add(self.l4_beach_umbrela_pole_1)
        self.scene.add(self.l4_beach_umbrela_1)
        self.scene.add(self.l4_beach_umbrela_pole_2)
        self.scene.add(self.l4_beach_umbrela_2)
        self.scene.add(self.l4_beach_umbrela_pole_3)
        self.scene.add(self.l4_beach_umbrela_3)
        self.scene.add(self.l4_beach_umbrela_pole_4)
        self.scene.add(self.l4_beach_umbrela_4)
        self.scene.add(self.l4_beach_umbrela_pole_5)
        self.scene.add(self.l4_beach_umbrela_5)
        self.scene.add(self.l4_beach_umbrela_pole_6)
        self.scene.add(self.l4_beach_umbrela_6)
        self.scene.add(self.l4_buoy_1)
        self.scene.add(self.l4_buoy_2)
        self.scene.add(self.l4_buoy_3)
        self.scene.add(self.l4_buoy_4)
        self.scene.add(self.l4_buoy_5)
        
        self.scene.add(self.beach_umbrella_person_1)
        self.scene.add(self.beach_umbrella_person_2)
        self.scene.add(self.beach_umbrella_person_3)
        self.scene.add(self.beach_umbrella_person_4)
        self.scene.add(self.beach_umbrella_person_5)
        self.scene.add(self.beach_umbrella_person_6)
        self.scene.add(self.buoy_person_1)
        self.scene.add(self.buoy_person_2)
        self.scene.add(self.buoy_person_3)
        self.scene.add(self.buoy_person_4)
        

        # Add Pages
        self.scene.add(self.game_cover)
        self.scene.add(self.instructions)
        self.scene.add(self.winning)
        self.scene.add(self.game_over)

        self.lives = 3
        self.angle = 0
        self.shooting = False
        self.level = 1
        self.go = True

        self.tiro = -1
        self.collision = False
        self.win = False
        self.wind = random.randint(1,2)
        self.winds.material.uniform_dict["tileNumber"].data = self.wind
        self.moveWind = 0

        #TARGET
        self.target = []
        self.target.append(bottle_builder())
        self.target.append(bottle_builder())
        self.target.append(bottle_builder())
        self.target.append(bottle_builder())
        self.target.append(bottle_builder())
        self.target.append(bottle_builder())
        self.target.append(bottle_builder())

        #self.target[1].translate(0.9, 0.3, -0.05)
        #self.target[2].translate(0.9, 0.3, -0.05)
        #self.target[3].translate(0.9, 0.3, -0.05)
        #self.target[4].translate(0.9, 0.3, -0.05)
        #self.target[5].translate(0.9, 0.3, -0.05)

        self.targetRig = []
        self.targetRig.append(TargetRig())
        self.targetRig.append(TargetRig())
        self.targetRig.append(TargetRig())
        self.targetRig.append(TargetRig())
        self.targetRig.append(TargetRig())
        self.targetRig.append(TargetRig())
        self.targetRig.append(TargetRig())

        
        self.targetRig[0].add(self.target[0])
        self.targetRig[1].add(self.target[1])
        self.targetRig[2].add(self.target[2])
        self.targetRig[3].add(self.target[3])
        self.targetRig[4].add(self.target[4])
        self.targetRig[5].add(self.target[5])
        self.targetRig[6].add(self.target[6])



        #NIVEL 1 ALVOS
        self.targetRig[0].set_position([0.19, 0.36, 5])
        self.targetRig[0].rotate_y(-math.pi/1.45)

        #NIVEL 2 ALVOS
        self.targetRig[1].set_position([903.19, 0.56, -23])
        self.targetRig[1].rotate_y(-math.pi/1.3)

        #NIVEL 3 ALVOS
        self.targetRig[2].set_position([605.19, 2.9, -20])
        self.targetRig[2].rotate_y(-math.pi/1.2)
        self.targetRig[3].set_position([594.81, 2.9, -15])
        self.targetRig[3].rotate_y(-math.pi/1.8)

        #NIVEL 4 ALVOS
        self.targetRig[4].set_position([305, 2.9, -20])
        self.targetRig[4].rotate_y(-math.pi/1.2)
        self.targetRig[5].set_position([296.3, 0.69, -16])
        self.targetRig[5].rotate_y(-math.pi/1.6)
        self.targetRig[6].set_position([311.5, 0.59, 2.8])
        self.targetRig[6].rotate_y(-math.pi/0.75)


        self.scene.add(self.targetRig[0])
        self.scene.add(self.targetRig[1])
        self.scene.add(self.targetRig[2])
        self.scene.add(self.targetRig[3])
        self.scene.add(self.targetRig[4])
        self.scene.add(self.targetRig[5])
        self.scene.add(self.targetRig[6])
        

        self.targetsCollided = []
        self.targetsCollided = [False for i in range(7)]
        
    def update(self):
        self.cameraRig.update(self.input, self.level, self.win)
        self.renderer.render(self.scene, self.camera)
        
        self.levels.material.uniform_dict["tileNumber"].data = self.level-1
        if self.cameraRig.isGame == True:
            self.win = False
            self.rig.update(self.input, self.delta_time)
            if self.go:
                if self.level == 1:
                    self.targetRig[0].set_position([0.19, 0.36, 5])
                    self.rig.set_position([0, 2, 20])
                if self.level == 2:
                    self.targetRig[1].set_position([903.19, 0.56, -23])
                    self.rig.set_position([900, 2 , 0])
                if self.level == 3:
                    self.targetRig[2].set_position([605.19, 2.9, -20])
                    self.targetRig[3].set_position([594.81, 2.9, -15])
                    self.rig.set_position([600, 2, 0])
                if self.level == 4:
                    self.targetRig[4].set_position([305, 2.9, -20])
                    self.targetRig[5].set_position([296.3, 0.69, -16])
                    self.targetRig[6].set_position([311.5, 0.59, 2.8])
                    self.rig.set_position([300, 2, 0])
                if self.level == 5:
                    self.level = 1
                    self.targetRig[0].set_position([0.19, 0.36, 5])
                    self.rig.set_position([0, 2, 20])
                self.rig._look_attachment.set_local_matrix(self.rig.getInitalMatrix())
                self.rig.rotate_y(-self.rig.getInitialRotation())
                self.rig.setInitialRotation(0)
                self.lives = 3
                self.tiro = -1
                self.frisbees[0].set_position([100, 100, 100])
                self.frisbees[1].set_position([100, 100, 100])
                self.frisbees[2].set_position([100, 100, 100])
                self.wind = random.randint(1,2)
                self.winds.material.uniform_dict["tileNumber"].data = self.wind
                if self.wind == 1:
                    self.moveWind = round(random.uniform(-0.001, -0.05), 3)
                else:
                    self.moveWind = round(random.uniform(0.001, 0.05), 3)
                self.go = False
            if self.collision == True:
                if self.level == 1 and self.targetsCollided[0] == True:
                    self.level = self.level + 1
                    self.go = True
                elif self.level == 2 and self.targetsCollided[1] == True:
                    self.level = self.level + 1
                    self.go = True
                elif self.level == 3 and self.targetsCollided[2] == True and self.targetsCollided[3] == True:
                    self.level = self.level + 1
                    self.go = True
                elif self.level == 4 and self.targetsCollided[4] == True and self.targetsCollided[5] == True and self.targetsCollided[6] == True:
                    self.rig.set_position([0, 2, 20])
                    self.rig._look_attachment.set_local_matrix(self.rig.getInitalMatrix())
                    self.rig.rotate_y(-self.rig.getInitialRotation())
                    self.rig.setInitialRotation(0)
                    self.rig.update(self.input, self.delta_time)
                    self.level = self.level + 1
                    self.win = True
                    self.go = True
                elif self.lives == 0:
                    self.rig.set_position([0, 2, 20])
                    self.rig._look_attachment.set_local_matrix(self.rig.getInitalMatrix())
                    self.rig.rotate_y(-self.rig.getInitialRotation())
                    self.rig.setInitialRotation(0)
                    self.rig.update(self.input, self.delta_time)
                    self.level = 5
                    self.targetsCollided = [False for i in range(7)]
                    self.go = True
                else:
                    self.go = False
                

            if self.rig.isShooting() == True and self.shooting == False:
                self.shooting = True
                self.frisbees[self.tiro].set_local_matrix(self.frisbee.global_matrix)
                self.lives = self.lives-1
                self.collision = False
            if self.rig.isShooting() == True and self.shooting == True:
                if self.rig.getPower() < 5:
                    self.angle = self.angle + 1/self.rig.getPower()*0.1
                elif self.rig.getPower() < 30:
                    self.angle = self.angle + 1/self.rig.getPower()*0.5
                else:
                    self.angle = self.angle + 1/self.rig.getPower()*1
                self.frisbees[self.tiro].translate(self.moveWind,self.rig.getPower()*0.008,math.cos(self.angle)-1)
            else:
                self.shooting = False
                self.angle = 0
                tileNumber = math.floor(self.rig.getPower() / 30)
                self.strength_bar.material.uniform_dict["tileNumber"].data = tileNumber
                tileNumber1 = self.lives
                self.n_frisbees.material.uniform_dict["tileNumber"].data = tileNumber1
                self.rig.update(self.input, self.delta_time)

        #COLLISION
        frisbeeCollision = self.frisbees[self.tiro].global_position
        
        targetCollision = []
        targetCollision.append(self.target[0].global_position)
        targetCollision.append(self.target[1].global_position)
        targetCollision.append(self.target[2].global_position)
        targetCollision.append(self.target[3].global_position)
        targetCollision.append(self.target[4].global_position)
        targetCollision.append(self.target[5].global_position)
        targetCollision.append(self.target[6].global_position)

        #TARGET 1
        vector1=np.array(frisbeeCollision)
        vector11=np.array(targetCollision[0])
        dist1= math.sqrt(abs((vector11[0]-vector1[0])**2+(vector11[1]-vector1[1])**2 +(vector11[2]-vector1[2])**2))

        #TARGET 2
        vector2=np.array(frisbeeCollision)
        vector21=np.array(targetCollision[1])
        dist2= math.sqrt(abs((vector21[0]-vector2[0])**2+(vector21[1]-vector2[1])**2 +(vector21[2]-vector2[2])**2))

        #TARGET 3
        vector3=np.array(frisbeeCollision)
        vector31=np.array(targetCollision[2])
        dist3= math.sqrt(abs((vector31[0]-vector3[0])**2+(vector31[1]-vector3[1])**2 +(vector31[2]-vector3[2])**2))

        #TARGET 4
        vector4=np.array(frisbeeCollision)
        vector41=np.array(targetCollision[3])
        dist4= math.sqrt(abs((vector41[0]-vector4[0])**2+(vector41[1]-vector4[1])**2 +(vector41[2]-vector4[2])**2))

        #TARGET 5
        vector5=np.array(frisbeeCollision)
        vector51=np.array(targetCollision[4])
        dist5= math.sqrt(abs((vector51[0]-vector5[0])**2+(vector51[1]-vector5[1])**2 +(vector51[2]-vector5[2])**2))

        #TARGET 6
        vector6=np.array(frisbeeCollision)
        vector61=np.array(targetCollision[5])
        dist6= math.sqrt(abs((vector61[0]-vector6[0])**2+(vector61[1]-vector6[1])**2 +(vector61[2]-vector6[2])**2))

        #TARGET 7
        vector7=np.array(frisbeeCollision)
        vector71=np.array(targetCollision[6])
        dist7= math.sqrt(abs((vector71[0]-vector7[0])**2+(vector71[1]-vector7[1])**2 +(vector71[2]-vector7[2])**2))

        #TARGET 1
        if dist1 <= 1.5:
            self.targetsCollided[0] = True
            self.targetRig[0].set_position([-10,-10,-10])
            self.hitSound.play()
            power = self.rig.getPower()
            self.rig.setPower(power/2)

        #TARGET 2
        if dist2 <= 1.5:
            self.targetsCollided[1] = True
            self.targetRig[1].set_position([-10,-10,-10])
            self.hitSound.play()
            power = self.rig.getPower()
            self.rig.setPower(power/2)
        
        #TARGET 3
        if dist3 <= 1.5:
            self.targetsCollided[2] = True
            self.targetRig[2].set_position([-10,-10,-10])
            self.hitSound.play()
            power = self.rig.getPower()
            self.rig.setPower(power/2)

        #TARGET 4
        if dist4 <= 1.5:
            self.targetsCollided[3] = True
            self.targetRig[3].set_position([-10,-10,-10])
            self.hitSound.play()
            power = self.rig.getPower()
            self.rig.setPower(power/2)

        #TARGET 5
        if dist5 <= 1.5:
            self.targetsCollided[4] = True
            self.targetRig[4].set_position([-10,-10,-10])
            self.hitSound.play()
            power = self.rig.getPower()
            self.rig.setPower(power/2)

        #TARGET 6
        if dist6 <= 1.5:
            self.targetsCollided[5] = True
            self.targetRig[5].set_position([-10,-10,-10])
            self.hitSound.play()
            power = self.rig.getPower()
            self.rig.setPower(power/2)

        #TARGET 7
        if dist7 <= 1.5:
            self.targetsCollided[6] = True
            self.targetRig[6].set_position([-10,-10,-10])
            self.hitSound.play()
            power = self.rig.getPower()
            self.rig.setPower(power/2)

        #Ground
        if self.frisbees[self.tiro].global_position[1] < 0.17:
            self.rig.setShooting(False)
            self.collision = True
            if self.tiro < 2:
                self.tiro = self.tiro + 1
                self.rig.setPower(0)


Game().run()