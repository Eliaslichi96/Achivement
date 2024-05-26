# Project Setup

## Prerequisites

### Python Installation

Install Python 3.8.7 on your system if you haven’t already. Verify the installation by running:

python --version

## Virtual Environment
Set up a new virtual environment named cf-python-base:

_python -m venv cf-python-base_

Activate the virtual environment:

* On Windows:
  * _cf-python-base\Scripts\activate_

* On macOS/Linux:
  - _source cf-python-base/bin/activate_

### Code Editor
Install Visual Studio Code or another text editor of your choice.

### Creating the Script
Create a script named add.py with the following functionality:

* Prompt the user to enter two numbers.
* Store the input in variables and add them.
* Print the result.

 ### add.py

* _a = int(input("Enter the first number: "))_
*  _b = int(input("Enter the second number: "))_
* _c = a + b_
* _print(f"The sum of {a} and {b} is {c}.")_

### Setting Up IPython
Install IPython in the cf-python-base virtual environment:

- _pip install ipython_

Verify the installation by launching IPython:
- _ipython_

### Exporting Requirements

Generate a requirements.txt file from your environment:

- _pip freeze > requirements.txt_

### Create a New Environment
Create a new environment named cf-python-copy and install the packages from requirements.txt:

Set up the new environment:

- _python -m venv cf-python-copy_

Activate the environment:

* On Windows:
  - _cf-python-copy\Scripts\activate_

* On macOS/Linux:
  - _source cf-python-copy/bin/activate_

Install the required packages:

- _pip install -r requirements.txt_
