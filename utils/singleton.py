# Extracted from https://stackoverflow.com/questions/6760685/what-is-the-best-way-of-implementing-singleton-in-python#:~:text=Method%203%3A%20A%20metaclass

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


# USAGE:
# class MyClass(BaseClass, metaclass=Singleton):
#    pass