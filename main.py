class Human:
	def __init__(self, name):
		self.name = name
		self.gender = 'None'
		self.age = 0
	def live(self):
		print(self.name, 'is alive')

class Parent(Human):
	def work():
		print('I can work')

class Child(Human):
	def happybirthday(self):
		self.age +=1 
		print('I am', self.age)
	def study(self):
		print(self.name,' can study')

obj = Child('Bob')
obj.study()
obj.live()
obj.happybirthday()
obj.happybirthday()
obj.happybirthday()