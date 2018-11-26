"""
Reference:
https://sourcemaking.com/design_patterns/strategy/python/1

Intent:
-------
- Define a family of algorithms, encapsulate each one, and make them interchangeable. Strategy
lets the algorithm vary INDEPENDENTLY from the CLIENTS that use it.

- Capture the abstraction in an interface, bury implementation details in derived classes.

How to:
--------
Encapsulate interface details in a base class, and bury implementation details in derived
classes. Clients can then couple themselves to an interface, and not have to experience
the upheaval associated with change: no impact when the number of derived classes changes,
and no impact when the implementation of a derived class changes.

Problem
-------
One of the dominant strategies of object-oriented design is the "open-closed principle".

Strategy scheme
---------------
A generic value of the software community for years has been, "maximize cohesion and
minimize coupling". This object-oriented design approach is all about minimizing coupling.
Since the client is coupled only to an abstraction (i.e. a useful fiction), and not a
particular realization of that abstraction, the client could be said to be practicing"
abstract coupling" . an object-oriented variant of the more generic exhortation
"minimize coupling".

A more popular characterization of this "abstract coupling" principle is:
"Program to an interface, not an implementation".

Clients should prefer the "additional level of indirection" that an interface
(or an abstract base class) affords. The interface captures the abstraction (i.e. the
"useful fiction") the client wants to exercise, and the implementations of that
interface are effectively hidden.

Structure
----------
The Interface entity could represent either an abstract base class, or the method
signature expectations by the client. In the former case, the inheritance hierarchy
represents dynamic polymorphism. In the latter case, the Interface entity represents
template code in the client and the inheritance hierarchy represents static polymorphism.

Check list
----------
1. Identify an algorithm (i.e. a behavior) that the client would prefer to access through
a "flex point".

2. Specify the signature for that algorithm in an interface.
3. Bury the alternative implementation details in derived classes.
4. Clients of the algorithm couple themselves to the interface.
"""

import abc


class Strategy(metaclass=abc.ABCMeta):
    """
    Declare an interface common to all supported algorithms. Context uses this interface
    to call the algorithm defined by a ConcreteStrategy.
    """
    @abc.abstractmethod
    def algorithm_interface(self):
        pass


class ConcreteStrategyA(Strategy):
    """
       Implement the algorithm using the Strategy interface.
    """
    
    def algorithm_interface(self):
        return "Algorithm A is implemented"


class ConcreteStrategyB(Strategy):
    """
        Implement the algorithm using the Strategy interface.
    """
    
    def algorithm_interface(self):
        return "Algorithm B is implemented"


class Context:
    """
    Define the interface of interest to clients. Maintain a reference to a Strategy object.
    """
    def __init__(self, strategy):
        self._strategy = strategy
        
    def client_interface_to_call_algo(self):
        return self._strategy.algorithm_interface()
    

# This is how Client uses the context interface, he has a say which algo he wants to use
concreate_strategy_a = ConcreteStrategyA()
context = Context(strategy=concreate_strategy_a)
assert "Algorithm A is implemented" == context.client_interface_to_call_algo()
