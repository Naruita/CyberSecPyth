class Fruit:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def get_fruit(self):
        self.name = input("Give the name of the fruit : ")
        self.price = int( input("What is the price of this fruit : "))

    def put_data(self):
        print(self.name)
        print(self.price)

class Banana(Fruit):

    def banana_prop(self):
        self.style = input("What kind of a fruit is {} : ".format(self.name))
    
    def banana_spew(self):
        print("Senor {} is a {} {}, who costs only {}.".format(self.name, self.style, self.name, self.price))

senor_fruit = Banana(None, None)
senor_fruit.get_fruit()
senor_fruit.banana_prop()
senor_fruit.banana_spew()
