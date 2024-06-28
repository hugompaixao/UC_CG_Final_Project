from core_ext.mesh import Mesh
from core_ext.texture import Texture

from geometry.rectangle import RectangleGeometry

from material.texture import TextureMaterial
from extras.text_texture import TextTexture

class GameCover(Mesh):
    def __init__(self):
        page = RectangleGeometry(1.5, 1)
        grid_texture = Texture(file_name="images/game.jpg")
        material = TextureMaterial(texture=grid_texture)
        self.mesh = Mesh(
            geometry = page,
            material = material
        )

        game_name = RectangleGeometry(0.75,0.25)
        game_name_texture = TextTexture(text="Frisbee Coastal Quest",
                               system_font_name="Wide Latin",
                               font_file_name = "fonts/Wide Latin Regular.ttf",
                               background_color=[255,255,255,0],
                               font_size=38, font_color=[0, 0, 0],
                               image_width=768, image_height=192,
                               align_horizontal=0.5, align_vertical=0.5,
                               image_border_width=0)
        game_name_material = TextureMaterial(game_name_texture)
        self.mesh3 = Mesh(game_name, game_name_material)

        inst_continue = RectangleGeometry(0.75,0.25)
        inst_continue_texture = TextTexture(text="Press [Enter] to Continue",
                               system_font_name="Algerian",
                               font_file_name = "fonts/ALGER.TTF",
                               background_color=[255,255,255,0],
                               font_size=40, font_color=[0, 0, 0],
                               image_width=768, image_height=256,
                               align_horizontal=0.5, align_vertical=0.5,
                               image_border_width=0)
        inst_continue_material = TextureMaterial(inst_continue_texture)
        self.mesh1 = Mesh(inst_continue, inst_continue_material)

        inst_exit = RectangleGeometry(0.75,0.25)
        inst_exit_texture = TextTexture(text="Press [Esc] to Quit",
                               system_font_name="Algerian",
                               font_file_name = "fonts/ALGER.TTF",
                               background_color=[255,255,255,0],
                               font_size=32, font_color=[0, 0, 0],
                               image_width=768, image_height=256,
                               align_horizontal=0.5, align_vertical=0.5,
                               image_border_width=0)
        inst_exit_material = TextureMaterial(inst_exit_texture)
        self.mesh2 = Mesh(inst_exit, inst_exit_material)

        
        
        self.mesh = super().__init__(page, material)
        self.mesh1 = Mesh(game_name, game_name_material)
        self.mesh1.translate(0,0.25,0.05)
        
        self.mesh2 = Mesh(inst_continue, inst_continue_material)
        self.mesh2.translate(0,0,0.05)

        self.mesh3 = Mesh(inst_exit, inst_exit_material)
        self.mesh3.translate(0,-0.1,0.05)

        

        self.add(self.mesh1)
        self.add(self.mesh2)
        self.add(self.mesh3)