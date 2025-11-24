I recently completed an automation project focused on applying Selenium WebDriver and the Page Object Model (POM) to build clean, maintainable browser tests for a sample web application (Urban Routes). This project strengthened my QA automation skills and gave me hands-on experience building a scalable test framework from the ground up.

Step 1: Implement Setup & Teardown Logic
Added class-level setup and teardown methods to initialise and close the Selenium WebDriver.
Ensured consistent test environment creation using pytest fixtures and class methods.

Step 2: Build a Dedicated Page Class (POM Architecture)
Created a new pages.py file containing the UrbanRoutesPage class.
Organised all Selenium imports, locators, and browser interaction logic into this reusable page object.

Step 3: Develop Full Page Object Model Functionality
Added all required element locators using By.ID, By.CLASS_NAME, By.XPATH, and additional strategies for dynamic elements.
Wrote methods in the page class to interact with the UI: element clicks, form inputs, navigation, and data retrieval.

Step 4:Execute End-to-End Automated Tests
Ran all tests with pytest to validate functionality and verify cross-browser interactions.
Ensured clean, error-free test runs and improved code structure for future test expansion.
