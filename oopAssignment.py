class Person:
  def __init__ (self,name,age,gender):
    self.name=name
    self.age=age
    self.gender=gender
    
  def introduce(self):
    print(f"My name is {self.name} I am {self.age} years old and I am a {self.gender}")
    
person1= Person("Wellington",27,"Male")
person1.introduce()