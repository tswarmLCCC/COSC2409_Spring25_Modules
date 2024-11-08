# Modules¶

If you quit from the Python interpreter and enter it again, the definitions you have made (functions and variables) are lost. Therefore, if you want to write a somewhat longer program, you are better off <u>using a text editor to prepare the input for the interpreter and running it with that file</u> as input instead. This is known as <u>creating a script</u>. As your program gets longer, you may want to split it into several files for easier maintenance. You may also want to use a handy function that you’ve written in several programs without copying its definition into each program.

To support this, Python has a way to <u>put definitions in a file and use them in a script or in an interactive instance of the interpreter</u>. Such a file is called a module; definitions from a module can be imported into other modules or into the <u>main module</u> (the collection of variables that you have access to in a script executed at the top level and in calculator mode).

A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py appended. Within a module, the module’s name (as a string) is available as the value of the global variable __name__. 

## Using Modules for more than Function Storage

A module can contain executable statements as well as function definitions. These statements are intended to initialize the module. They are executed only the first time the module name is encountered in an import statement.  (They are also run if the file is executed as a script.)

Each module has its own private namespace, which is used as the global namespace by all functions defined in the module. Thus, the author of a module can use global variables in the module without worrying about accidental clashes with a user’s global variables. On the other hand, if you know what you are doing you can touch a module’s global variables with the same notation used to refer to its functions, modname.itemname.

Modules can import other modules. It is customary but not required to place all import statements at the beginning of a module (or script, for that matter). The imported module names, if placed at the top level of a module (outside any functions or classes), are added to the module’s global namespace.

## Executable Modules

When you run a Python module with

```python
python fibo.py <arguments>
```

the code in the module will be executed, just as if you imported it, but with the __name__ set to "__main__". That means that by adding this code at the end of your module:

```python
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
```


you can make the file usable as a script as well as an importable module, because the code that parses the command line only runs if the module is executed as the “main” file:

```python
python fibo.py 50
```

0 1 1 2 3 5 8 13 21 34

If the module is imported, the code is not run:

```python
import fibo
```

This is often used either to provide a convenient user interface to a module, or for testing purposes (running the module as a script executes a test suite).

## Namespaces

In Python, a namespace is a container that holds unique names for objects like variables and functions. Each module has its own namespace, which helps avoid naming conflicts. This means you can use the same name in different modules without issues.

Modules can import other modules, and it's common to place import statements at the beginning of a file. Imported modules are added to the global namespace of the importing module.

For efficiency, a module is only imported once per session. To reload a module after changes, use `importlib.reload()`, e.g., `import importlib; importlib.reload(modulename)`.

Each module has its own private namespace, which is used as the global namespace by all functions defined in the module. Thus, the author of a module can use global variables in the module without worrying about accidental clashes with a user’s global variables. On the other hand, if you know what you are doing you can touch a module’s global variables with the same notation used to refer to its functions, modname.itemname.

Modules can import other modules. It is customary but not required to place all import statements at the beginning of a module (or script, for that matter). The imported module names, if placed at the top level of a module (outside any functions or classes), are added to the module’s global namespace.

For efficiency reasons, each module is only imported once per interpreter session. Therefore, if you change your modules, you must restart the interpreter – or, if it’s just one module you want to test interactively, use importlib.reload(), e.g. import importlib; importlib.reload(modulename).

Note - these lecture notes were adapted partially from https://docs.python.org/3/tutorial/modules.html, and excellent walkthrough of the use of modules.  We have combined several sources to build a more complete workflow to eventually include modules, documentation, object oriented practices, and unit testing.