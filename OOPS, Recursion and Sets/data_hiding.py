class Example_class:
    __hidden_variable = 0 ## double underscores are used to make the variable hidden and unable to access from outside.
    
    def add(self, increment):
        self.__hidden_variable += increment
        print(self.__hidden_variable)

test = Example_class()
test.add(5)
# print(test.__hidden_variable) #