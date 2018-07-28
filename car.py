from vehicle import vehicle

class car(vehicle):
	ac = "off"
	steering_wheel = "steady"
	seatbelt = "unlocked"
	audio_player = "off"

	def __init__(self, drift, deploy_airbags,no_of_wheels, speed, weight, mileage, color):
		self.drift = drift
		self.deploy_airbags = deploy_airbags
		super().__init__(no_of_wheels, speed, weight, mileage, color)

	def drift(self):
		print("car is drifting")

	def deploy_airbags(self):
		print("airbags is deployed")


