import math

class Vector:
    def __init__(self, position = [0, 0]) -> None:
        self.position = position # set the vector's position
	    
	self.magnitude = 0
	self.direction = []
	    
	self.updated() # update the vectors magnitude and direction

    def update(self):
	self.magnitude, self.direction = self.get(self.position) # get the vector's magintude and direction
	
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

    # get the vector's position based off a magnitude and direction
    def to(self, magnitude : float, directions : list):
        vector = [magnitude * direction for direction in directions]
        return vector
