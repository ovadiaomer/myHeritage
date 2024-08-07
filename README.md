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

