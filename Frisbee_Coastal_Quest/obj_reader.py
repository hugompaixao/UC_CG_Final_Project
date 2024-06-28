def obj_reader(filename: str):
    """Get the vertices, texture coordinates, and faces from the file"""
    vertices = []
    uvs = []
    position_list = []
    uv_list = []

    with open(filename, 'r') as in_file:
        for line in in_file:
            if line.startswith('v '):  # Vertex positions
                parts = line.strip().split()
                point = [float(value) for value in parts[1:]]
                vertices.append(point)
            elif line.startswith('vt '):  # Texture coordinates
                parts = line.strip().split()
                uv = [float(value) for value in parts[1:]]
                uvs.append(uv)
            elif line.startswith('f '):  # Faces
                parts = line.strip().split()
                for part in parts[1:]:
                    vertex_index, uv_index = [int(idx) if idx else 0 for idx in (part.split('/') + [None, None])[:2]]
                    position_list.append(vertices[vertex_index - 1])  # OBJ indices start at 1
                    if uvs:
                        uv_list.append(uvs[uv_index - 1] if uv_index else [0, 0])  # Handle missing UVs gracefully

    return {'vertices': position_list, 'uvs': uv_list}

# Test the function
if __name__ == '__main__':
    f_in = input("File? ")
    result = my_obj_reader(f_in)
    print("Vertices:", result['vertices'][:10])  # Show first 10 for brevity
    print("UVs:", result['uvs'][:10])  # Show first 10 for brevity
