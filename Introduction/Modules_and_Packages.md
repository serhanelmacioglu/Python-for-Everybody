# Modules and Packages

<br>

+ ## Modules

#### What's module?
- A Python file with functions, classes and other components

#### Why use modules?
- Break code down into reusable structures

<br>

### Creating a module

``` python

# helpers.py
def display(message, is_warning=False):
    if is_warning:
        print('Warning!!')
    print(message)
    
``` 
<br>

### Importing a module
[Modules](https://docs.python.org/3/tutorial/modules.html) allow you to store reusable blocks of code, such as functions, in separate files. They're referenced by using the `import` statement.

``` python

# import module as namespace
import helpers
helpers.display('Not a warning')

# import all into current namespace
from helpers import *
display('Not a warning')

# import specific items into current namespace
from helpers import display
display('Not a warning')
```
<br>
<br>
<br>

+ ## Packages

#### What are packages?
- Published collections of module

#### How do I find packages?
- Python Package Index
- Internet search   

<br>

### Installing packages
[Distribution packages](https://packaging.python.org/glossary/#term-distribution-package) are external archive files which contain resources such as classes and functions. Most every application you create will make use of one or more packages. Imports from packages follow the same syntax as modules you've created. The [Python Package index](https://pypi.org/) contains a full list of packages you can install using [pip](https://pip.pypa.io/en/stable/).

``` python

# Install an individual package
pip install colorama

# Install from a list of packages
pip install -r requirements.txt

# requirements.txt
colorama
```
