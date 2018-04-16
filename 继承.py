class Animal(object):
    def eat(self):
        print("eat")

    def run(self):
        print("run")

class B(object):
   def mark(self):
       print("mark")

class Dog(Animal,B):
  def mark(self):
      print("remark")
      super().mark()
      # B.mark(self)

Dog().mark()
