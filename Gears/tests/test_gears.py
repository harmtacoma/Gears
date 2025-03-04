import numpy as np
from Gears import generate_gear_vertices  # Adjust import to your file structure

def test_generate_gear_vertices():
    vertices = generate_gear_vertices(teeth=12, radius=1.0)
    assert isinstance(vertices, np.ndarray)
    assert vertices.shape[1] == 2  # Should be an array of (x, y) pairs