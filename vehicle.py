class vehicle():
	no_of_wheels = 0
	speed = 0
	weight = 0
	milage = 0
	colour ='blue'
	
	def __init__(self,no_of_wheels,speed,weight,milage,colour):
		self.no_of_wheels = no_of_wheels
		self.speed = speed
		self.weight=weight
		self.milage=milage
		self.colour=colour

	def go_forward(self):
		print("The Vehicle with {0} wheels has started moving.".format(self.no_of_wheels))
