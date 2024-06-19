class Dog:
  # Class attribute
  attr1 = "mammal"

  # Initialize the dog with a name
  def __init__(self, name):
    self.name = name  # Instance attribute

# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

# Accessing class attributes
print("Rodger is a {}".format(Rodger.__class__.attr1))
print("Tommy is also a {}".format(Tommy.__class__.attr1))

# Accessing instance attributes
print("My name is {}".format(Rodger.name))
print("My name is {}".format(Tommy.name))
