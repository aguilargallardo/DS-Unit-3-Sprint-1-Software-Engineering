class Product:
  """
  Class for products.
  """
  def __init__(self, name):
    import random as random
    self.name = name
    self.price = 10
    self.weight = 20
    self.flammability = .5
    self.identifier = random.randint(1000000, 9999999)


  def stealability(self):
   x = (self.price / self.weight)
   if x < 0.5:
     print("Not so stealable.")
   elif x >= 0.5 and x > 1.0:
     print("Kinda stealable.")
   else:
     print("Very stealable!")


  def explode(self):
    y = (self.flammability * self.weight)
    if y < 10:
      print("...fizzle.")
    elif y >= 10 and y < 50:
      print("...boom!")
    else:
      print("...BABOOM!!")





class BoxingGlove(Product):
  def __intit__(self, name = None, price = 10, weight = 10,
                flammability=0.5,
                identifier = 1):
      super().__init__(name=name, price=price, weight=weight,
                     flammability=flammability,
                     identifier=identifier)

  def explode(self):
    return print("...it's a glove.")

  def punch(self):
    z = self.weight
    if z < 5:
      print("That tickles.")
    elif z >= 5 and z < 15:
      print("Hey that hurt!")
    else:
      print("OUCH!")
