# MyHeritage Subscription Automation Project

## Overview

This project is an automation framework designed for navigating to Google, searching for "MyHeritage", clicking on the appropriate link, and performing actions on the MyHeritage website, including navigating to the price list, selecting a specific currency, and verifying subscription plans. The framework utilizes the Page Object Model (POM) design pattern with modular components and follows clean coding practices.

## Project Structure


### Components

- **`src/pages/`**: Contains page object classes using the Page Object Model (POM) pattern.
  - **`base_page.py`**: Base class for common web interactions.
  - **`google_search_page.py`**: Handles Google search and interactions.
  - **`myheritage_home_page.py`**: Contains methods for interacting with the MyHeritage homepage.
  - **`myheritage_price_list_page.py`**: Contains methods for interacting with the MyHeritage price list.
  - **`page_factory.py`**: Provides lazy-loaded access to page objects.

- **`src/utils/`**: Utility modules for data processing and file operations.
  - **`file_utils.py`**: Contains functions for file operations, such as saving sorted plans.
  - **`test_helpers.py`**: Contains helper functions used across tests.

- **`tests/`**: Contains test cases and configurations.
  - **`conftest.py`**: Pytest fixture configuration for setting up WebDriver and page initialization.
  - **`test_myheritage_subscription.py`**: Test case for verifying MyHeritage subscription plans.

- **`requirements.txt`**: Project dependencies.

## Installation

1. Clone the repository.
2. Navigate to the project directory.
3. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate

4. Install requirements
    ```bash
   pip install -r requirements.txt

## Running the Tests
To execute the tests, use the pytest command from the project /tests folder
(Test reports and results will be generated, with sorted plans being saved in tests/results):
  ```bash
  pytest

