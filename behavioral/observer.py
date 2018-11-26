"""
Intent:
-------
- Define a one-to-many dependency between objects so that when one object changes state,
  all its dependents are notified and updated automatically.
  
- Encapsulate the core (or common or engine) components in a Subject abstraction, and
  the variable (or optional or user interface) components in an Observer hierarchy.
  
- The "View" part of Model-View-Controller.

Problem:
--------
A large monolithic design does not scale well as new graphing or monitoring requirements
are levied.

Discussion:
------------
Define an object that is the "keeper" of the data model and/or business logic (the Subject).
Delegate all "view" functionality to decoupled and distinct Observer objects. Observers
register themselves with the Subject as they are created. Whenever the Subject changes,
it broadcasts to all registered Observers that it has changed, and each Observer queries
the Subject for that subset of the Subject's state that it is responsible for monitoring.

This allows the number and "type" of "view" objects to be configured dynamically, instead
of being statically specified at compile-time.

The protocol described above specifies a "pull" interaction model. Instead of the Subject
"pushing" what has changed to all Observers, each Observer is responsible for "pulling"
its particular "window of interest" from the Subject. The "push" model compromises reuse,
while the "pull" model is less efficient.

Subject represents the core (or independent or common or engine) abstraction. Observer
represents the variable (or dependent or optional or user interface) abstraction. The
Subject prompts the Observer objects to do their thing. Each Observer can call back to
the Subject as needed.

Summary:
---------
Define a one-to-many dependency between objects so that when one object
changes state, all its dependents are notified and update automatically.
"""

# The following program demonstrates how subject and observers can sync therir state using
# Observer design pattern.

import abc


class Subject:
    """
    Know its observers. Any number of Observer objects may observe a subject.
    Send a notification to its observers when its state changes.
    """
    def __init__(self):
        self._subject_state = None
        self._observers = set()
    
    def _notify(self, arg):
        for observer in self._observers:
            observer.update(arg)
    
    def register(self, observer):
        self._observers.add(observer)
        observer._subject = self
    
    def de_register(self, observer):
        self._observers.discard(observer)
        observer._subject = None
    
    @property
    def subject_state(self):
        return self._subject_state
    
    @subject_state.setter
    def subject_state(self, arg):
        self._subject_state = arg
        self._notify(arg)


class Observer(metaclass=abc.ABCMeta):
    """
    Define an updating interface for objects that should be notified of
    changes in a subject.
    """
    def __init__(self):
        self._observer_state = None
        self._subject = None
    
    @abc.abstractmethod
    def update(self, args):
        pass


class ConcreteObserver(Observer):
    """
    Implement the Observer updating interface to keep its state
    consistent with the subject's.
    Store state that should stay consistent with the subject's.
    """
    def push(self, arg):
        self._subject.subject_state = arg
        
    def update(self, arg):
        self._observer_state = arg
        

subject = Subject()
concrete_observer1 = ConcreteObserver()
concrete_observer2 = ConcreteObserver()
subject.register(concrete_observer1)
subject.register(concrete_observer2)

# This protocol described specifies a "pull" interaction model.
# observers pull from subject. Subject "pushing" what has changed to all Observers
subject.subject_state = 'hello'
assert concrete_observer1._observer_state == 'hello'
assert concrete_observer2._observer_state == 'hello'


# "push" interaction model: observers push to subject
# Observer is responsible for "pulling" its particular "window of interest" from the
# Subject. The "push" model compromises reuse, while the "pull" model is less efficient.
concrete_observer1.push('hello1')
assert concrete_observer2._observer_state == 'hello1'
assert subject.subject_state == 'hello1'

# de-registering
subject.de_register(concrete_observer2)
subject.subject_state = 'hello2'
assert concrete_observer1._observer_state == 'hello2'
assert concrete_observer2._subject is None
