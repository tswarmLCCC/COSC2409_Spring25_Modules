# Packages

In Python, a package is a way of structuring Python’s module namespace by using “dotted module names”. For example, the module name `A.B` designates a submodule named `B` in a package named `A`. Just like modules help avoid name clashes between global variables, packages help avoid name clashes between module names.

## Creating a Package

A package is simply a directory that contains a special file named `__init__.py` and other module files. The `__init__.py` file can be empty, but it must be present in the directory to indicate to Python that the directory is a package. Here’s an example of a simple package structure:

```
mypackage/
    __init__.py
    module1.py
    module2.py
```

You can import modules from this package using the dotted module name:

```python
import mypackage.module1
import mypackage.module2
```

Or you can import specific functions or classes from the modules:

```python
from mypackage.module1 import my_function
from mypackage.module2 import MyClass
```

## Using Packages

Packages can contain sub-packages, which are directories within the main package directory. Here’s an example of a package with a sub-package:

```
mypackage/
    __init__.py
    module1.py
    subpackage/
        __init__.py
        module2.py
```

You can import modules from the sub-package using the full dotted path:

```python
import mypackage.subpackage.module2
```

Or import specific functions or classes:

```python
from mypackage.subpackage.module2 import another_function
```

## Executable Packages

You can make a package executable by including a `__main__.py` file in the package directory. When you run the package with the `-m` option, the code in `__main__.py` will be executed:

```
mypackage/
    __init__.py
    __main__.py
    module1.py
```

Run the package:

```sh
python -m mypackage
```

## Namespaces in Packages

Just like modules, packages have their own namespaces. This helps avoid naming conflicts between modules in different packages. Each module within a package has its own namespace, and you can access the module’s functions and classes using the dotted module name.

## Importing from Packages

When you import a package, Python searches for the package in the directories listed in `sys.path`. You can add directories to `sys.path` at runtime if needed:

```python
import sys
sys.path.append('/path/to/your/package')
import mypackage
```

## Reloading Modules in Packages

For efficiency, a module is only imported once per session. To reload a module after changes, use `importlib.reload()`:

```python
import importlib
import mypackage.module1
importlib.reload(mypackage.module1)
```

## Summary

Packages are a powerful way to organize and structure your Python code, especially for larger projects. They help avoid naming conflicts and make it easier to manage and maintain your code. By using packages, you can create a clean and modular codebase that is easy to navigate and extend.

Note - these lecture notes were adapted partially from https://docs.python.org/3/tutorial/modules.html, and excellent walkthrough of the use of modules and packages. We have combined several sources to build a more complete workflow to eventually include packages, documentation, object-oriented practices, and unit testing.