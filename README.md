# Project Name : Assignment
UI and REST hybrid automation
## How to use
Root directory of the project: assignment. There are to markers divided as sanity and regression, sanity has the base use case and regression has other use cases
command to run
> pytest -m {marker}
> ex: pytest -m sanity

## Directory structure
1. config - Has the config or more like properties file
2. pages - Has page locators and actions
3. test - Has all the test class files
		-conftest.py - Has setup and teardown defined
		-BaseTest.py - Requests the fixute for setup, all test files should use BaseTest as parent class to be able to request setup fixture.
4. reports - Test exectuion report is saved in this directory with report.html name
5. pytest.ini - file has default command line options to run pytest command

## References
- HTML parser referece - https://docs.python-guide.org/scenarios/scrape/#lxml-and-requests
- String split and join back - https://www.kite.com/python/answers/how-to-remove-spaces,-tabs,-and-newlines-in-a-string-in-python
- HTML-report documentation - https://pytest-html.readthedocs.io/en/latest/