
class Vector:
	def __init__(self, position : list = None) -> None:
		self.position = position

	def get(self):
		return self.position
		
	def get_form(self):
		return self.to_form(self.get())
		
	def to_form(self, vector):
		magnitude = math.sqrt(sum(component ** 2 for component in vector))
        
		if magnitude == 0:
			directions = [0 for _ in vector]
		else:
			directions = [component / magnitude for component in vector]
		# indent test
