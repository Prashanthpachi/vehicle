from vehicle import vehicle

class bike(vehicle):
	handle = True
	is_gear =True
	def __init__(self,handle,is_gear,no_of_wheels,speed,weight,milage,colour):
		self.handle=handle
		self.is_gear=is_gear
		vehicle.__init__(self,no_of_wheels,speed,weight,milage,colour)

	def wheele(self):
		print("The bike has started a wheele on back wheele")

	def stoopie(self):
		print("Stunt done")
