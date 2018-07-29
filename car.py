from vehicle import vehicle

class car(vehicle):
	ac = False
	steering_wheel = True
	seat_belt = True
	audio_player=True
	def __init__(self,ac,steering_wheel,seat_belt,audio_player,no_of_wheels,speed,weight,milage,colour):
		self.ac =ac
		self.steering_wheel =steering_wheel
		self.seat_belt = seat_belt
		self.audio_player=audio_player
		vehicle.__init__(self,no_of_wheels,speed,weight,milage,colour)

	def drift(self):
		print("Car's Drifting")
