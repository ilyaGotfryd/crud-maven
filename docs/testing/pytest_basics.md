As in any self respecting language Python has a number of powerful test suits. My personal favorite is PyTest. It provides for very clean test code and supports everything you need in a test framework including clear and ellaborate error reporting. It is a very mature framework with excellent plugins for coverage, async testing, TDD workflow, etc.

Here we are going to set pytest up and return to Pydantic for further applied exploration.

Install PyTest via PIP:
```bash
pip install pytest
```

* Create `test` folder in root folder.
* Inside `test` folder create a `__init__.py`. It is **double underscore** also reffered to as **dunder**. With newer versions of puthon this file is no longer necessary, however it used to indicate that a particular folder is actually a module. If this file included into a module folder it could betreated as constructor of sorts for the module and will be executed any time anything is imported for that module. In case of `pytest` `__init__.py` is used in folder structure to indicate all the related folders down to the root of test suit. This allows us to import modules from outside of test suit.
* create `test_service.py` in the `test` folder. That will be our service test file. Pytest will know to include it because it starts with `test_` prefix.
* functions inside test file need to have prefix of `test_` as well to be included into test suit.


[Back to Pydantic](../pydantic/pydantic.md)