"""
Intent:
-------
- Ensure a class has only one instance, and provide a global point of access to it.
- Encapsulated "just-in-time initialization" or "initialization on first use".

Problem:
--------
Application needs one, and only one, instance of an object. Additionally, lazy initialization and
global access are necessary.

Problem:
--------
Application needs one, and only one, instance of an object. Additionally, lazy initialization and
global access are necessary.

Singleton should be considered only if all three of the following criteria are satisfied:
-----------------------------------------------------------------------------------------
- Ownership of the single instance cannot be reasonably assigned
- Lazy initialization is desirable
- Global access is not otherwise provided for
- If ownership of the single instance, when and how initialization occurs, and global access are
  not issues, Singleton is not sufficiently interesting.

The Singleton pattern can be extended to support access to an application-specific number of
instances.
"""
import threading


class Singleton:
    __singleton_lock = threading.Lock()
    __app_instance = None
    
    def __init__(self):
        pass
    
    @classmethod
    def get_cls_instance(cls):
        if not cls.__app_instance:
            cls.__singleton_lock.acquire()
            if not cls.__app_instance:
                cls.__app_instance = Singleton()
            cls.__singleton_lock.release()

        return cls.__app_instance


# If you want to get an instance of Singleton class, do not call the class directly but instead
# ALWAYS call the class method that takes care of creation of Singleton object.
s1 = Singleton.get_cls_instance()
s2 = Singleton.get_cls_instance()
assert s1 == s2
