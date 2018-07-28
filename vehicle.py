class vehicle:

	no_of_wheels = 0
	speed = 0
	weight = 0
	mileage = 0
	color = 0

	def __init__(self, no_of_wheels, speed, weight, mileage, color):
		self.no_of_wheels = no_of_wheels
		self.speed = speed
		self.weight = weight
		self.mileage = mileage
		self.color = color

	def go_forward(self):
		print("The vehicle with {0} wheels has started moving forward".format(self.no_of_wheels))

	def go_reverse(self):
		print("The vehicle with {0} wheels has started moving reverse".format(self.no_of_wheels))

	def stop(self):
		print("The vehicle has stopped")



