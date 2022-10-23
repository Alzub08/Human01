#class Human:
#	def __init__(self, name):
	#	self.name = name
	#	self.gender = 'None'
	#	self.age = 0
	#def live(self):
	#	print(self.name, 'is alive')
	#def happybirthday(self):
	#	self.age +=1 
	#	print('I am', self.age)
	#def eat(self):
	#	print('I am eating')

#class Parent(Human):
#	def work(self):
	#	print(self.name,' can work')
#	def eat(self):
#		super().eat()
	#	print('It is apple')

#class Child(Human):
#	def study(self):
	#	print(self.name,' can study')

#child1 = Child('Bob')

 #child1.study()
 #child1.live()
 #child1.happybirthday()
 #child1.happybirthday()
 #child1.happybirthday()

#parent1 = Parent('Jane')
#child1.eat()
#parent1.eat()
# parent1.work()
# parent1.eat()
 #for i in range(30):
 #	parent1.happybirthday()
# a = 4
 #print('a')
# print(a)
# if a == 5:
 #	print('if 1')
# elif a > 3:
 #	print('if 2')
# elif a < 6:
# 	print('if 3')
# a = 0
# while a<5:
# 	print('hi')
# 	a = a + 1
# for i in range(5):
# 	print(i)
# print('Hello world')
# print('This is my first commit')

 #class Human:
# 	def __init__(self):
# 		self.name = 'None'
# 		self.age = 0
# 		self.gender = 'None'
# 	def introduce(self):
# 		print('Hello, my name is', self.name)
# 	def add_info(self):
# 		self.name = input('Name: ')
# 		self.age = int(input('Age: '))
# 		self.gender = input('Gender: ')

class Animal:
  def __init__(self, name):
    self.name = name
    self.gender = 'None'
    self.age = 0
  def live(self):
    print(self.name, 'is alive')
  def eat(self):
    print('I am eating')
  
    
class Kat(Animal):
  def __init__(self, name):
    self.name = name
    self.gender = 'None'
    self.age = 0
  def sleap(self):
    print(self.name,' can sleap')
  def eat(self):
    super().eat()
    print('It is fish')
  def speak(self):
    print('Miaau') 
    
class Dog(Animal):
  def __init__(self, name):
    self.name = name
    self.gender = 'None'
    self.age = 0
  def play(self):
    print(self.name,' can playing')
  def eat(self):
    super().eat()
    print('It is meat')
  def speak(self):
    print(self.name,' gaw-gavv')

class Hamster(Animal):
  def __init__(self, name):
    self.name = name
    self.gender = 'None'
    self.age = 0
  def chil(self):
    print(self.name,' can chiling')
  def eat(self):
    super().eat()
    print('It is tomato')
  def speak(self):
    print(self.name,' hrhrhr')

kat1 = Kat('Murka')
dog1 = Dog('Garry')
hamster1 = Hamster('Chiller')

odj1 = Kat('Murka')
odj1.eat()
odj1.sleap()
odj1.speak()
odj1 = Dog('Garry')
odj1.eat()
odj1.play()
odj1.speak()
odj1 = Hamster('Chiller')
odj1.eat()
odj1.chil()
odj1.speak()

# obj = Human('')
# obj = Animal('')
# obj.introduce()
# obj.add_info()
# obj.introduce()



