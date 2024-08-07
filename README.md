# ESH Home Assignment

## Overview

This project contains the implementation of a login functionality test using Playwright with Python. It includes automated tests for valid and invalid login attempts

## Prerequisites

- Python 3.8 or higher
- Git

## Setup

### Clone the Repository

#### Using HTTPS and Personal Access Token

bash:
```git clone https://github.com/ovadiaomer/esh_home_assignment```
cd esh_home_assignment

Install Dependencies:
```pip install -r requirements.txt```

Install playwright:
```playwright install```

Project Structure:

    src/: Source code
        components/: UI components and helpers
            button.py: Button component for interacting with buttons in the tests.
            locator.py: Locator base class for element selection.
            text_input.py: TextInput component for interacting with input fields.
        config/: Configuration files
            config.py: General configuration settings.
            credentials.py: Credentials used for testing.
        pages/: Page objects
            login_page.py: Page object model for the login page.
    tests/: Test cases
        conftest.py: Pytest fixtures for setting up the test environment.
        test_login.py: Test cases for login functionality.
    requirements.txt: Python dependencies (to install)
    README.md: Project documentation.

## Fixtures 

 - The conftest.py file contains fixtures that set up the testing environment. Here’s a brief explanation of the fixtures:

 - browser(): Initializes a Playwright browser instance. 

 - page(browser): Creates a new page in the initialized browser for each test function. 

 - username() and password(): Provide the default username and password for the tests.

These fixtures ensure that each test runs in a fresh environment, preventing state leakage between tests.

## Page Classes
Page classes encapsulate the structure and actions of web pages. This follows the Page Object Model (POM) design pattern, which enhances maintainability and readability. The login_page.py file is an example of a page class.

Here’s a brief explanation of the LoginPage class:

LoginPage: Contains methods to interact with the login page elements, such as filling in the username and password fields and clicking the login button. It helps to keep the tests clean and readable.