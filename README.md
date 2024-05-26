# Project Setup

## Prerequisites

### Python Installation

Install Python 3.8.7 on your system if you haven’t already. Verify the installation by running:

python --version

## Virtual Environment
Set up a new virtual environment named cf-python-base:

- python -m venv cf-python-base

Activate the virtual environment:

* On Windows:
- cf-python-base\Scripts\activate

* On macOS/Linux:
- source cf-python-base/bin/activate

### Code Editor
Install Visual Studio Code or another text editor of your choice.

### Creating the Script
Create a script named add.py with the following functionality:

* Prompt the user to enter two numbers.
* Store the input in variables and add them.
* Print the result.

# add.py

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = a + b
print(f"The sum of {a} and {b} is {c}.")

### Setting Up IPython
Install IPython in the cf-python-base virtual environment:

- pip install ipython

Verify the installation by launching IPython:
- ipython

### Exporting Requirements

Generate a requirements.txt file from your environment:

- pip freeze > requirements.txt

### Create a New Environment
Create a new environment named cf-python-copy and install the packages from requirements.txt:

Set up the new environment:

- python -m venv cf-python-copy

Activate the environment:

* On Windows:
- cf-python-copy\Scripts\activate

* On macOS/Linux:
- source cf-python-copy/bin/activate

Install the required packages:

- pip install -r requirements.txt
