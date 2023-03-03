Before running the development environment for the first time, you must create a virtual environment

Create virtual environment for backend development

```python3 -m venv venv```

Activate the virtual environment by

```source venv/bin/activate```

If you are done with development, you can deactivate by

```deactivate```

Once you activate the virtual environment, install the dependencies

```pip install -r requirements.txt```

The main reason we use virtual environments in each project is to isolate the dependencies for each project, that way unexpected errors are avoided.