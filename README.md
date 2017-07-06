# pylogdctr
Simple decorator for Python3 classes that adds a class level logger instance.

Provides the `@logs` decorator for classes.  `@logs` adds a Logger to each decorated class by adding a new member
variable `self._log`.  The logger is automatically named by module + classname. i.e. `mypackage.mymodule.MyClass`.


### Usage
#### Code (mymodule.py)
    import logging
    import pylogdctr


    @pylogdctr.logs
    class MyClass:
        def some_function(self):
            self._log.debug("Debug Message.")

    """ Set up the logging stream and format: """
    ch = logging.StreamHandler(sys.stdout)
    ch.setFormatter(logging.Formatter("{name}({levelname:<5}): {message}", style="{"))
    logging.root.addHandler(ch)
    logging.getLogger(f"__module__.MyClass").setLevel(logging.DEBUG)

    mc = MyClass()
    mc.some_function()

#### Yields
    mymodule.MyClass(DEBUG): Debug Message.
