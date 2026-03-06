# mobile_app_testing_with_appium
Pytest framework based on Page Object Model using appium+python+allure for app created to work with 
SimpleLogin app for android and Ios. This  automation framework is structured using Page Object Model (POM) 
and Fixtures. It is designed to accommodate multiple types of tests like E2E, Functional, Compatibility, 
Reliability tests within framework. The framework is built with scalability and extensibility in mind to 
add more test types with enhanced maintainability, reusability and also by separating concerns 
(e.g., test logic, page objects, and test data), the framework makes it easier to manage and scale 
as the application grows.

**Automated Testing Framework Design**

    1. Hybrid Framework: Combines the benefits of data-driven and keyword-driven approaches to achieve flexibility and maintainability.

    2. Modular and Layered Architecture:Each layer of the framework is decoupled, meaning that changes in one layer (e.g., page object or locators) do not directly affect the other layers.
        Layer 1: Test Data Layer: Stores the test data (cases.json or excel etc)
        Layer 2: Page Object Layer: Page classes that encapsulate UI elements and methods to interact with those elements.
        Layer 3: Test Logic Layer: Includes the test actions that drive the interactions, calling methods from the page classes.
        Layer 4: Test Runner Layer: The entry point to initiate test execution, manage setup and teardown and other configurations.
        Layer 5: Test Report Layer: Generate detailed test reports after execution that include passed, failed, and skipped test cases.
    
    3. Test Execution Flow: The test execution process will be managed through a test runner like pytest, nose, junit, testng etc.

**Test Architecture and Tools:**

    1. Tool & Language: Appium with Python and Selenium bindings
    2. Design Pattern: Page Object Model (POM)
    3. Testing Framework(Hybrid): Combines data-driven and keyword-driven.
    4. Continuous Integration: Jenkins/GitHub Actions (Can Integrate)

**Why Appium with Python bindings?:**

    1. Appium enables automation testing for mobile apps (Android and iOS) using a single framework.
    2. It supports multiple programming languages (Python, Java, JavaScript, etc.) through the WebDriver protocol, 
       making it flexible for different teams.
    3. It allows testing of native, hybrid, and mobile web applications without modifying the app source code.
    4. It uses the WebDriver protocol, and the Selenium Python bindings implement that protocol, allowing 
       Python code to control mobile apps the same way Selenium controls web browsers.
    5. Using Python + Selenium bindings provides stable WebDriver APIs, better compatibility, and reusable automation 
       patterns (e.g., Page Object Model, waits, locators).
    6. It enables cross-platform mobile automation (Android/iOS) with familiar Selenium-style commands while leveraging 
       Python’s simplicity and large testing ecosystem.

**Framework Structure:**
    
      ├── app           # applications files(*.apk and *.ipa)
      ├── pages         # Page Object Model (POM) classes(Ui and actions) 
          ├── locators  # Page object repository(ui locators)
          ├── ui        # Page classes that encapsulate ui elements 
          ├── action    # classes and methods to interact with those elements. 
      ├── data          # Test data files
      ├── log           # generate test logs 
      ├── reports       # generated reports etc
      ├── utils         # Utility classes (e.g., helper, logger etc)
      ├── tests         # test runner files to initiate test execution
      pytest.ini        # init files
      README.md         # Instruction file.
      requirement.txt   # install dependencies

**Task description:**

    1.  Download the SimpleLogin app(Android(*.apk) and Ios(*.ipa))
    2.  Create test plan for SimpleLogin app (12 test cases)
         ![Testcases](img.png)
    3. Create pytest framework based on design pattern(POM - Page Object Model):
        - Appium
        - Python
        - Allure
        - pytest
    4.  Instructions given below for prerequisites and setup, description of project, how to run tests

**Prerequisites and Setup istructions for Andriod and Ios:**

    1. Python 3.12 (https://www.python.org/downloads/)
    2. Install requirements `pip install -r requirements.txt`

**Andriod**

    1. Appium Server (https://github.com/appium/appium-desktop/releases/tag/v1.22.3-4)
    2. Android Studio/SDK (https://developer.android.com/studio/install)
    3. Install android device emulator via device manager or plug real device
    4. Run android device (if you are working with emulator check plugged devices via cmd `adb devices` and copy current device name)
    5. Run appium server

**IOS (Must need Mac OS)**

    1. Appium Server (https://github.com/appium/appium-desktop/releases/tag/v1.22.3-4)
    2. Install Xcode from App store to select simulator or plug real device 
    3. Install Carthage and set up WebDriverAgent
    4. Use Xcode to provisioning profile/Signing for WDAgentRunner target
    5. Run appium server

**How to run tests in project:**

    1. Check current device name in conftest.py. If device name is not match with `CURRENT_DEVICE` change variable
       value to device name and details
    2. Run tests for android (example: `pytest test_android.py --runmode=local --alluredir=reports/allure-results or --html-report=./report/pytest_html_report.html`)
    3. Run tests for ios (example: `pytest test_ios.py --runmode=local --alluredir=reports/allure-results or --html-report=./report/pytest_html_report.html')

**To Run in device farms(Browserstack, saucelabs, Aws devicefarms etc):**

    1. Check browserstack set in conftest.py correcly. If device name is not match with `BROWSERSTACK_DEVICES` change variable
       value to correct device name, credentials  and app details.
    2. Run tests for android (example: `pytest test_android.py --runmode=browserstack --alluredir=reports/allure-results or --html-report=./report/pytest_html_report.html`)
    3. Run tests for ios (example: `pytest test_ios.py --runmode=browserstack --alluredir=reports/allure-results or --html-report=./report/pytest_html_report.html')

**To Run in parallel with multiple devices either with Browserstack or locally:**

    1. Local : pytest -n 2 --runmode=local --alluredir=reports/allure-results or --html-report=./report/pytest_html_report.html.
    2. Browserstack : pytest -n 2 --runmode=browserstack --alluredir=reports/allure-results or --html-report=./report/pytest_html_report.html
    

**Other Report Formats**

    1. Html Report : pytest test_*.py --html=./report/testreport.html
    2. pytest-htmlreporter : pytest test_*.py --html-report=./report/pytest_html_report.html
    3. Allure Report : pytest test_*.py --alluredir=reports/allure-results
       (a). Collect allure report using command below to get this need to install allure commandline utility and enjoy results!
            1. allure generate reports/allure-results -o reports/allure-report --clean
            2. allure open reports/allure-report

