# The 'Munroe Meter' Jargon Scoring System

## Getting started as a developer

It is best practice to work on Python projects within a virtual environment,
to avoid conflicts with your main system installation. The `virtualenv` tool
can be installed following the instructions at
https://virtualenv.pypa.io/en/stable/installation/

Clone this Git repository, then navigate to the folder where you cloned it
in a terminal and run the following sequence of commands to set up a virtual
environment and install all the project's dependencies.

```
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
pip install -r test_requirements.txt  # For testing
```

You can then install the project package itself in 'developer mode', so that
changes made to files in your working copy are reflected in the installed
package too:

```
pip install -e .
```

### Testing

Testing is being done using [pytest][pytest]. To run all the tests, just use

```
pytest test
```

New tests should be written in files inside the `test` folder, named either
`test_*.py` or `*_test.py`. The tests themselves are functions with names
starting `test_` and taking no arguments. They check expected behaviour using
`assert` statements.

See the [pytest documentation][test-discovery] for more details.

### Updating requirements

The `requirements.txt` file used above is generated from a specification in
`requirements.in` by [pip-tools][pip-tools]. This ensures that we list the
exact versions used of all our dependencies, including indirect ones. If you
are adding a new dependency, add it to `requirements.in` and then run

```
pip install pip-tools  # First time only!
pip-compile
```

To upgrade dependencies to their latest versions use

```
pip-compile --upgrade
```

## Download static file

```
bower install
```

## Flash

```
python runserver.py
```

[pytest]: http://doc.pytest.org/en/latest/contents.html
[pip-tools]: https://github.com/nvie/pip-tools
[test-discovery]: http://doc.pytest.org/en/latest/goodpractices.html#test-discovery
