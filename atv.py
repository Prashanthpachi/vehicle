from bike import bike
from car import car

class atv(bike,car):
	fuel_used ='Petrol'
	def __init__(self,fuel_used,handle,is_gear,ac,steering_wheel,seat_belt,audio_player,no_of_wheels,speed,weight,milage,colour):
		self.fuel_used =fuel_used
		bike.__init__(self,handle,is_gear,no_of_wheels,speed,weight,milage,colour)
		car.__init__(self,ac,steering_wheel,seat_belt,audio_player,no_of_wheels,speed,weight,milage,colour)
	
	def features(self):
		print("Its an hybrid of Car and Bike")
