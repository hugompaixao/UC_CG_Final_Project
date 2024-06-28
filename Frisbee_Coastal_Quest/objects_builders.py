from obj_reader import obj_reader

from core_ext.mesh import Mesh
from core_ext.texture import Texture

from material.texture import TextureMaterial
from geometry.rectangle import RectangleGeometry
from geometry.sphere import SphereGeometry
from geometry.objects import objectsGeometry
import random


def sky_builder():
    sky_geometry = SphereGeometry(radius=99)
    sky_material = TextureMaterial(
        texture =Texture(file_name="images/sky1.jpg")
    )
    return Mesh(sky_geometry, sky_material)


def ground_builder():
    ground_geometry = RectangleGeometry(width=200, height=200)
    ground_material = TextureMaterial(
        texture = Texture(file_name="images/sand.jpg"),
        property_dict = {"repeatUV": [50, 50]}
    )
    return Mesh(ground_geometry, ground_material)


def sea_builder():
    sea_obj = obj_reader('objects/sea.obj')
    sea_geometry = objectsGeometry(vertex_data=sea_obj['vertices'], color_data=[0, 0, 0], uv_data=sea_obj['uvs'])
    sea_material = TextureMaterial (
        texture = Texture(file_name="images/sea.jpg"),
        property_dict = {"repeatUV": [1000, 1000]}
    )
    return Mesh(sea_geometry, sea_material)


# Palmtree build = log + leafs
def log_builder():
    log_obj = obj_reader('objects/tree.obj')
    log_geometry = objectsGeometry(vertex_data=log_obj['vertices'], color_data=[0, 0, 0], uv_data=log_obj['uvs'])
    log_material = TextureMaterial(
        texture = Texture(file_name="images/log.jpg"),
        #property_dict = {"repeatUV": [1, 1]}
    ) 
    return Mesh(log_geometry, log_material)

def leafs_builder():
    leafs_obj = obj_reader('objects/leaf.obj')
    leafs_geometry = objectsGeometry(vertex_data=leafs_obj['vertices'], color_data=[0, 0, 0], uv_data=leafs_obj['uvs'])
    leafs_material = TextureMaterial(
        texture = Texture(file_name="images/leaf_green.jpg"),
        property_dict = {"repeatUV": [50, 50]}
    ) 
    return Mesh(leafs_geometry, leafs_material)


def small_rock_builder():
    small_rock_obj = obj_reader('objects/rock.obj')
    small_rock_geometry = objectsGeometry(vertex_data=small_rock_obj['vertices'], color_data=[0, 0, 0], uv_data=small_rock_obj['uvs'])
    small_rock_material = TextureMaterial (
        texture = Texture(file_name="images/rock.jpg"),
        #property_dict = {"repeatUV": [100, 100]}
    ) 
    return Mesh(small_rock_geometry, small_rock_material)
    

def big_rock_builder():
    big_rock_obj = obj_reader('objects/sea_stone.obj')
    big_rock_geometry = objectsGeometry(vertex_data=big_rock_obj['vertices'], color_data=[0, 0, 0], uv_data=big_rock_obj['uvs'])
    big_rock_material = TextureMaterial (
        texture = Texture(file_name="images/rock.jpg"),
        #property_dict = {"repeatUV": [100, 100]}
    ) 
    return Mesh(big_rock_geometry, big_rock_material)


def frisbee_builder():
    frisbee_obj = obj_reader('objects/frisbee_up.obj')
    frizbee_geometry = objectsGeometry(vertex_data=frisbee_obj['vertices'], color_data=[0, 0, 0], uv_data=frisbee_obj['uvs'])
    frizbee_material = TextureMaterial (
        texture = Texture(file_name="images/frisbeeblue.jpg"),
        property_dict = {"repeatUV": [100, 100]}
    ) 
    return Mesh(frizbee_geometry, frizbee_material)

def bottle_builder():
    bottle_obj = obj_reader('objects/bottle.obj')
    bottle_geometry = objectsGeometry(vertex_data=bottle_obj['vertices'], color_data=[0, 0, 0], uv_data=bottle_obj['uvs'])
    bottle_material = TextureMaterial(
        texture = Texture(file_name="images/frize.jpg"),
    ) 
    return Mesh(bottle_geometry, bottle_material)


def buoy_builder():
    buoy_obj = obj_reader('objects/boia.obj')
    buoy_geometry = objectsGeometry(vertex_data=buoy_obj['vertices'], color_data=[0, 0, 0], uv_data=buoy_obj['uvs'])
    buoy_material = TextureMaterial(
        texture = Texture(file_name="images/boia.png"),
    ) 
    return Mesh(buoy_geometry, buoy_material)

# Flag build = pole + flag
def flag_pole_builder():
    pole_obj = obj_reader('objects/poste.obj')
    pole_geometry = objectsGeometry(vertex_data=pole_obj['vertices'], color_data=[0, 0, 0], uv_data=pole_obj['uvs'])
    pole_material = TextureMaterial(
        texture = Texture(file_name="images/white.jpg"),
        property_dict = {"repeatUV": [50, 50]}
    ) 
    return Mesh(pole_geometry, pole_material)

def flag_builder():
    flag_obj = obj_reader('objects/bandeira.obj')
    flag_geometry = objectsGeometry(vertex_data=flag_obj['vertices'], color_data=[0, 0, 0], uv_data=flag_obj['uvs'])
    flag_material = TextureMaterial(
        texture = Texture(file_name="images/red.jpg"),
        property_dict = {"repeatUV": [50, 50]}
    ) 
    return Mesh(flag_geometry, flag_material)

# Beach Umbrela = umbrela pole + umbrela 
def beach_umbrela_pole_builder():
    pole_obj = obj_reader('objects/gsp.obj')
    pole_geometry = objectsGeometry(vertex_data=pole_obj['vertices'], color_data=[0, 0, 0], uv_data=pole_obj['uvs'])
    pole_material = TextureMaterial(
        texture = Texture(file_name="images/white.jpg"),
        property_dict = {"repeatUV": [50, 50]}
    ) 
    return Mesh(pole_geometry, pole_material)

def beach_umbrela_builder():
    beach_umbrela_obj = obj_reader('objects/gs.obj')
    beach_umbrela_geometry = objectsGeometry(vertex_data=beach_umbrela_obj['vertices'], color_data=[0, 0, 0], uv_data=beach_umbrela_obj['uvs'])
    beach_umbrela_material = TextureMaterial(
        texture = Texture(file_name="images/red.jpg"),
        property_dict = {"repeatUV": [50, 50]}
    ) 
    return Mesh(beach_umbrela_geometry, beach_umbrela_material)

def cooler_builder():
    cooler_obj = obj_reader('objects/cooler.obj')
    cooler_geometry = objectsGeometry(vertex_data=cooler_obj['vertices'], color_data=[0, 0, 0], uv_data=cooler_obj['uvs'])
    cooler_material = TextureMaterial(
        texture = Texture(file_name="images/boia.png"),
        property_dict = {"repeatUV": [50, 50]}
    ) 
    return Mesh(cooler_geometry, cooler_material)

def person_up_builder():
    person_up_obj = obj_reader('objects/p_up.obj')
    person_up_geometry = objectsGeometry(vertex_data=person_up_obj['vertices'], color_data=[0, 0, 0], uv_data=person_up_obj['uvs'])
    person_up_material = TextureMaterial(
        texture = Texture(file_name="images/person.jpg"),
        #property_dict = {"repeatUV": [50, 50]}
    ) 
    return Mesh(person_up_geometry, person_up_material)


def person_down_builder():
    person_down_obj = obj_reader('objects/p_down.obj')
    person_down_geometry = objectsGeometry(vertex_data=person_down_obj['vertices'], color_data=[0, 0, 0], uv_data=person_down_obj['uvs'])
    person_down_material = TextureMaterial(
        texture = Texture(file_name="images/person.jpg"),
        #property_dict = {"repeatUV": [50, 50]}
    ) 
    return Mesh(person_down_geometry, person_down_material)