__author__ = "ChiangWei"
__date__ = "2022/04/25"

# Import threading module.
import threading


# # Create singleton class with a decorator
# def singleton(cls, *args, **kwargs):
#     instance = None

#     def __singleton(*args, **kwargs):
#         nonlocal instance
#         if instance == None:
#             instance = cls(*args, **kwargs)
#         return instance

#     return __singleton


# Create singleton class with a decorator
# Singleton Decorator.
def singleton(cls):
    # Get lock instance for each class that uses this decorator.
    lock = threading.Lock()
    # The instance variable temporary storage instance of cls.
    instance = None

    def __singleton(*args, **kwargs):
        # Get externally declared variables.
        nonlocal lock
        nonlocal instance

        # Avoid double writes.
        if instance is None:
            with lock:
                if instance is None:
                    # Get instance object.
                    instance = cls(*args, **kwargs)

        # Return instance object.
        return instance

    # Return inner function.
    return __singleton


@singleton
class Singleton:
    pass


SingletonA = Singleton()
SingletonB = Singleton()

print(SingletonA)
print(SingletonB)

print(SingletonA == SingletonB)

print(type(Singleton()))
