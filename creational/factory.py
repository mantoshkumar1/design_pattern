"""
Intent
-------
Define an interface for creating an object, but let subclasses decide which class to
instantiate. Factory Method lets a class defer instantiation to subclasses.

People often use Factory Method as the standard way to create objects; but it isn't
necessary if: the class that's instantiated never changes, or instantiation takes
place in an operation that subclasses can easily override (such as an initialization
operation).

The client is totally decoupled from the implementation details of derived classes.
Polymorphic creation is now possible.

The Factory Method defines an interface for creating objects, but lets subclasses
decide which classes to instantiate.

Summary:
--------
Define an interface for creating an object, but let subclasses decide which class to
instantiate. Factory Method lets a class defer instantiation to subclasses.

Consider making all constructors private or protect. Some Factory Method advocates recommend
that as a matter of language design (or failing that, as a matter of style) absolutely all
constructors should be private or protected. It's no one else's business whether a class
manufactures a new object or recycles an old one. The new operator considered harmful. There
is a difference between requesting an object and creating one. The new operator always creates
an object, and fails to encapsulate object creation. A Factory Method enforces that
encapsulation, and allows an object to be requested without inextricable coupling to the
act of creation.

The advantage of a Factory Method is that it can return the same instance multiple times, or can
return a subclass rather than an object of that exact type.
"""

import abc

# it is important to write metaclass here


class Creator(metaclass=abc.ABCMeta):
    """
    Declare the factory method, which returns an object of type Product.
    Creator may also define a default implementation of the factory
    method that returns a default ConcreteProduct object.
    Call the factory method to create a Product object.
    """
    def __init__(self):
        self.product = self._factory_method()
    
    @abc.abstractmethod
    def _factory_method(self):
        pass
    
    def client_uses_this_api_to_call_product_function(self):
        return self.product.interface()


class ConcreteCreatorA(Creator):
    """
    Override the factory method to return an instance of a
    ConcreteProduct1.
    """
    def _factory_method(self):
        return ConcreteProductA()


class ConcreteCreatorB(Creator):
    """
    Override the factory method to return an instance of a
    ConcreteProduct2.
    """
    def _factory_method(self):
        return ConcreteProductB()


class Product(metaclass=abc.ABCMeta):
    """
    Define the interface of objects the factory method creates.
    """
    @abc.abstractmethod
    def interface(self):
        pass

    def common_function(self):
        return "Product: common function"


class ConcreteProductA(Product):
    """
    Implement the Product interface.
    """
    def interface(self):
        return "Concrete Product A"


class ConcreteProductB(Product):
    """
    Implement the Product interface.
    """
    def interface(self):
        return "Concrete Product B"


# This is how Client uses the context interface, he does not initiate the product but let
# application decide which subclass to initiate.

# Example 1
concrete_creator = ConcreteCreatorA()
assert "Concrete Product A" == concrete_creator.client_uses_this_api_to_call_product_function()
assert "Product: common function" == concrete_creator.product.common_function()

# Example 2
concrete_creator = ConcreteCreatorB()
assert "Concrete Product B" == concrete_creator.client_uses_this_api_to_call_product_function()
assert "Product: common function" == concrete_creator.product.common_function()
