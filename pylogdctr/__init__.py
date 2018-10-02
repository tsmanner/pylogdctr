"""
Defines the `logs` decorator.

`@logs` adds a Logger to each decorated class by adding a new member variable `self._log`.
The logger is automatically named by module + classname. i.e. `mypackage.mymodule.MyClass`.

Usage (mymodule.py):

@logs
class MyClass:
    def some_function(self):
        self._log.debug("Debug Message.")  # self._log.name is "mymodule.MyClass"
"""
import logging


def logs(cls):
    cls._log = logging.getLogger("{modulename}.{classname}".format(modulename=cls.__module__, classname=cls.__name__))
    return cls
