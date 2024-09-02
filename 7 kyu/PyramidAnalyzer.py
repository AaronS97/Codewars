##  In this kata, you are given the sum of the number of vertices, edges, and faces of an N-sided pyramid, which is equal to s. You need to return the number of vertices, edges, faces, and the number of sides of the base of the pyramid.
def pyramid(s):
    edges = int((s / 2) - 1)
    sides = int(s // 4)
    vertices = int(sides + 1)
    faces = vertices
    return vertices, edges, faces, sides