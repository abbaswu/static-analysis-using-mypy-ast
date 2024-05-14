# Static Analysis Using mypy's AST

Perform static analysis on a Python project using mypy's AST (which involves parsing Python files and performing [semantic analysis](https://mypy-lang.blogspot.com/2019/07/mypy-0720-released.html), including name resolution, on the parsed Python files).

NOTE: MUST USE PYTHON 3.7 AND MYPY<0.730 (released 2019-09-26). To install:

- Set up a Python 3.7 environment.
- Install [`pypi-timemachine`](https://github.com/astrofrog/pypi-timemachine) to enable installing packages released before a specific date.
- Using `pypi-timemachine`, install `mypy` and any other Python packages released before 2019-09-26.
