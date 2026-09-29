# What Is a Virtual Environment and Why Use It?

A **Python virtual environment** is an isolated workspace on your computer. It allows you to have a dedicated installation of Python and its packages for a specific project, completely separate from your global system Python and other projects.

## Why Use a Virtual Environment?

Virtual environments are useful because they:

- Keep project dependencies isolated from other projects.
- Prevent package version conflicts.
- Keep your global Python environment clean.
- Allow different projects to use different package versions.
- Make projects easier to share and reproduce.

---

## Creating a Virtual Environment

Use the following command to create a virtual environment:
syntax

```
python -m venv environment_name # for windows and mac
# example
python -m venv env

```

Use the following command to activate the virtual environment
syntax

```
# For windows
./environment_name/Scripts/activate

# for Mac/linux
source environment_name/bin/activate

```

## Installation Fast API

Installing the fast api standard version using pip

```
pip install  "fastapi[standard]"
```

## Running the Server

```
fastapi dev main.py
```

## `__init__.py` in Python

### What is `__init__.py`?

`__init__.py` is a special Python file used inside a folder to define that folder as a **Python package**.

Example:

my_fastapi_app/
├── main.py
└── routers/
├── **init**.py
├── users.py
└── products.py

The `routers` folder contains `__init__.py`, so Python can treat it as a package.

---

## Why do we use it?

It allows us to organize Python code into packages and import modules from those packages.

For example:

```python
from routers.users import router
```
