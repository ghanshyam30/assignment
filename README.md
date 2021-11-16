# Project Name : Assignment
UI and REST hybrid automation

## Pre-requisites
1. User's system should have at least python3.7 installed.
2. Along with python3, pipenv should be already installed.

## How to use
Root directory of the project: assignment, so all the commands to be fired should be executed after navigating to the assignment directory. There are two markers divided as smoke and regression, smoke has the base use case and regression has other use cases.

**Command to setup**
> pipenv install .

### Update REPO_LIST
1. Update REPO_LIST from config\config.py file to have all account names you want to test.
2. This REPO_LIST acts as the parameter for the somke test, so we can execute it like for 100 or so times for different accounts.

**Command to run test**
> pytest -m {marker}

> ex: pytest -m smoke

## Directory structure
1. additonalLibraries - Has functionality other than selenium or rest library.
2. config - Has the config or more like properties file.
3. pages - Has page locators and actions.
4. drivers - Has the driver bin file.
5. test - Has all the test class files.
		-conftest.py - Has setup and teardown defined
		-BaseTest.py - Requests the fixute for setup, all test files should use BaseTest as parent class to be able to request setup fixture.
6. reports - Test exectuion report is saved in this directory with report.html name
7. pytest.ini - file has default command line options to run pytest command

## References
- HTML parser referece - https://docs.python-guide.org/scenarios/scrape/#lxml-and-requests
- String split and join back - https://www.kite.com/python/answers/how-to-remove-spaces,-tabs,-and-newlines-in-a-string-in-python
- HTML-report documentation - https://pytest-html.readthedocs.io/en/latest/
- Video tutorial reference - https://youtu.be/qBK5I_QApCg