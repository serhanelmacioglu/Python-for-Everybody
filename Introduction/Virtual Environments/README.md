## Virtual environments
[Virtual environments](https://docs.python.org/3.7/tutorial/venv.html) allow you to install packages into an isolated folder. This allows you to better manage versions.


#### By default, packages are installed globally
Version management becomes a challenge

#### Virtual environments can be used to contain and manage package collections
Really just a folder behind the scenes with all your packages

<br>

### Installing virtual environment

``` python

# Install virtual environment
pip install virtualenv

# Windows system
python -m venv <folder_name>

# OSX/Linux (bash)
virtualenv <folder_name>

```

<br>

### Using virtual environment

``` python

# Windows systems
# cmd.exe
<folder_name>\Scripts\Activate.bat
# Powershell
<folder_name>\Scripts\Activate.ps1
# bash shell
. ./<folder_name>/Scripts/activate

# OSX/Linux (bash)
<folder_name>/bin/activate

```

<br>

### Installing packages in a virtual environment

``` python

# Install an individual package
pip install colorama

# Install from a list of packages 
pip install -r requirements.txt

# requirements.txt
colorama

```

