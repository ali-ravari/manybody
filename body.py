

"""
This class generates the position and velocity of the body (asteroid, planet, etc.)
"""
class body:
    def __init__(self, name: str, mass : int, position, velocity):
        self.name = name
        self.mass = mass
        self.position = position
        self.velosity = velocity


m1 = body("m1", 20000000, (0,102,1452),(124,1556,6542))
print(m1.position)