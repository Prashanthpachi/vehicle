from vehicle import vehicle

class truck(vehicle):
	max_load = 100000
	speed_limit = 60
	
	def __init__(self, max_load, speed_limit,no_of_wheels, speed, weight, mileage, color):
		self.max_load = max_load
		self.speed_limit = speed_limit
		super().__init__(no_of_wheels, speed, weight, mileage, color)

	def load(self):
		print("truck is loaded")

	def unload(self):
		print("truck is unloaded")


