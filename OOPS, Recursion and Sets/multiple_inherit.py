class A:
    def a_method(self):
        print("This is a method from class A")

class B:
    def b_method(self):
        print("This is a method from class B")

class C(A, B):
    def c_method(self):
        print("This is a method from class C")

class D(C):
    def d_method(self):
        print("Class is from D-kun, yo.")

c_boi = C()
c_boi.a_method()
c_boi.b_method()
c_boi.c_method()
print("Multiple Inheritance done.")

D_boi = D()
D_boi.a_method()
D_boi.b_method()
D_boi.c_method()
D_boi.d_method()
print("Multi Level Inheritance done.")
