from geometry.geometry import Geometry
from core.attribute import Attribute

class objectsGeometry(Geometry):
    def __init__(self, vertex_data, color_data, uv_data):
        #def __init__(self, vertex_data, color_data):
        super().__init__()
        # Extract vertex positions from the vertex_data list
        vertex_positions = vertex_data
        vertex_colors = color_data
        # Extract UV texture coordinates from the provided data
        uv_coordinates = uv_data
        # Add attributes to the hat geometry
        self.add_attribute("vec3", "vertexPosition", vertex_positions)
        self.add_attribute("vec3", "vertexColor", vertex_colors)
        self.add_attribute("vec2","vertexUV", uv_coordinates)
        #self.count_vertices()

