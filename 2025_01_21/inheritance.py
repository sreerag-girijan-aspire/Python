class Parent:
    pass
class Child(Parent): #Single Inheritance: A child class inherits from one parent class.
    pass




class Parent1:
    pass

class Parent2:
    pass

class Child(Parent1, Parent2): #Multiple Inheritance: A child class inherits from more than one parent class.
    pass



class Grandparent:
    pass

class Parent(Grandparent):
    pass

class Child(Parent): #Multilevel Inheritance: A class is derived from another derived class.
    pass




class Parent:
    pass

class Child1(Parent):
    pass

class Child2(Parent): #Hierarchical Inheritance: Multiple classes inherit from a single parent class.
    pass
