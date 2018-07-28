from vehicle import vehicle

class bike(vehicle):
	handle = 0
	is_gear = 0

	def __init__(self, handle, is_gear,no_of_wheels, speed, weight, mileage, color):
		self.handle =handle
		self.is_gear =is_gear
		super().__init__(no_of_wheels, speed, weight, mileage, color)

	def wheelie(self):
		print("the bike started wheelie")

	def stoppie(self):
		print("the bike has stopped")



