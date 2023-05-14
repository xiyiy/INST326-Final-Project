import math

class Car:
	def __init__(self, x = 0, y = 0, heading = 0):
		"""Sets the three attributes x, y, and heading to the values 
			of their corresponding parameters

		Args: 
			self: reference to the current instance of the class
			x(float): the starting x coordinate of the car, default: 0
			y(float): the starting y coordinate of the car, default: 0
			heading(float): the starting heading, default: 0
		"""
		self.x = x
		self.y = y
		self.heading = heading

	def turn(self, degrees):
		"""Calculates the direction in which car drives, in degrees

		Args: 
			self: reference to the current instance of the class
			degrees(float): number of degrees

		Side effects: 
			replaces the previous value in heading with the calculation

		Return: self.heading (float)
		
		"""
		self.degrees = degrees
		self.heading = (self.heading + degrees) % 360

		return self.heading

	def drive(self, dist):
		"""Determining the x and y location to drive the car forward

		Args: 
			self: reference to the current instance of the class
			dist(float): distance the car will travel
			d(float): assigned to distance
			h(float): changes heading to radians
		
		Side effects: 
			Chnages the x and y positions
			changes the value of headings to radians 
			heading is set to h

		"""
		self.dist = dist
		d = self.dist
		h = self.heading * (math.pi/180)

		self.x += d*math.sin(h)
		self.y -= d*math.cos(h)

def sanity_check():
	"""Creates an instance of the car class
	Displays the location and heading of the car

		Args: no args 

		Side effects: 
			changes x and y positions of the car and the degrees it turns
			printing location and heading of the car

		Return: an instance of the car class
	"""

	VroomVroom = Car()

	VroomVroom.turn(90)
	VroomVroom.drive(10)
	VroomVroom.turn(30)
	VroomVroom.drive(20)

	print(VroomVroom.x, VroomVroom.y)
	print(VroomVroom.heading)

	return VroomVroom

if __name__ == "__main__": sanity_check()





