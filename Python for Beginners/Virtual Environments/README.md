## Virtual environments

<br>

[Virtual environments](https://docs.python.org/3.7/tutorial/venv.html) allow you to install packages into an isolated folder. This allows you to better manage versions.

- #### By default, packages are installed globally
    Version management becomes a challenge

- #### Virtual environments can be used to contain and manage package collections
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

<br>

###### Please note: If you have any problem when you are trying to generate venv in VS Code, then type that " Set-ExecutionPolicy RemoteSigned " at the PowerShell terminal. Bear in mind that VS Code must be run as administrator before you type this " Set-ExecutionPolicy RemoteSigned ". 
###### [How to start VS Code as administrator?](https://docs.microsoft.com/en-us/visualstudio/ide/user-permissions-and-visual-studio?view=vs-2019#:~:text=On%20the%20Windows%20desktop%2C%20right,and%20then%20select%20OK%20again.) On the Windows desktop, right-click the Visual Studio shortcut and then select Properties. Select the Advanced button, and then select the Run as Administrator check box. Select OK, and then select OK again.
