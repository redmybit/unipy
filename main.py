import math

# infinite dimension vector class
class Vector:
    def __init__(self, components = [0, 0]) -> None:
        self.components = components # set the vector's components
	    
        self.magnitude = 0
        self.direction = []

        self.updated() # update the vectors magnitude and direction

    # updates the vector's magnitude and direction based off it's components
    def update(self):
	    self.magnitude, self.direction = self.get(self.components) # get the vector's magintude and direction
	
    # get the vector in magnitude and direction form
    def get(self, vector : list):
        magnitude = math.sqrt(sum(component ** 2 for component in vector))
    
        # avoid division by zero
        if magnitude == 0:
            directions = [0 for _ in vector]
        else:
            # normalize each component to find directions
            directions = [component / magnitude for component in vector]
        
        return directions, magnitude

    # get the vector's components based off a magnitude and direction
    def to(self, magnitude : float, directions : list):
        components = [magnitude * direction for direction in directions]
        return components

    # checks if the vectors have the same length
    def check(self, vector):
        if len(self.components) != len(vector.components):
            # throw an error
            raise ValueError("Vectors must have the same number of dimensions to add.")

        return true

    # function for adding the vectors
    def __add__(self, other):
        # check if the vectors have the same length
        self.check(other)

        # component-wise addition
        added_components = [a + b for a, b in zip(self.components, other.components)]
        return Vector(added_components)

    # string-representation of a vector
    def __repr__(self):
        return f"Vector({self.components})"
