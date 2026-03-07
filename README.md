# mobile_app_testing_with_appium
A **Pytest-based automation framework** built using the **Page Object Model (POM)** with **Appium, Python, and Allure reporting** has been developed to test the **SimpleLogin mobile application for Mobile platforms(Android/iOS)**.

The framework is structured around **POM and Pytest fixtures**, enabling clear separation of responsibilities and better test organization. It supports multiple categories of testing, including **End-to-End (E2E), Functional, Compatibility, and Reliability testing** within a unified framework.

Designed with **scalability and extensibility** in mind, the framework allows additional test types to be integrated easily. By separating components such as **test logic, page objects, and test data**, it improves **maintainability, reusability, and overall test management**, making it easier to scale as the application evolves.


**Automated Testing Framework Design**

1. **Hybrid Framework:**
   The framework follows a **hybrid approach**, combining the strengths of **data-driven and keyword-driven testing** to provide greater **flexibility, reusability, and maintainability**.

2. **Modular and Layered Architecture:**
   The framework is designed with a **decoupled, layered architecture**, ensuring that modifications in one layer (such as page objects or locators) do not impact other layers directly.

   * **Layer 1 – Test Data Layer:**
     Maintains test data sources such as **JSON files, Excel sheets, or other external data repositories**.

   * **Layer 2 – Page Object Layer:**
     Contains **page classes** that encapsulate **UI elements (locators)** and the **methods required to interact with those elements**.

   * **Layer 3 – Test Logic Layer:**
     Implements **test scenarios and actions**, invoking methods from the **page object classes** to perform application interactions.

   * **Layer 4 – Test Runner Layer:**
     Acts as the **entry point for test execution**, responsible for **initialization, configuration, setup, teardown, and execution management**.

   * **Layer 5 – Test Report Layer:**
     Responsible for generating **comprehensive test execution reports** that provide insights into test results, failures, and overall execution metrics.

3. **Test Execution Flow:**
   Test execution is orchestrated using a **test runner framework such as Pytest, Nose, JUnit, or TestNG**, which manages **test discovery, execution, reporting, and lifecycle hooks**.


**Test Architecture and Tools:**

    1. Tool & Language: Appium with Python and Selenium bindings
    2. Design Pattern: Page Object Model (POM)
    3. Testing Framework(Hybrid): Combines data-driven and keyword-driven.
    4. Continuous Integration: Jenkins/GitHub Actions (Can Integrate)

**Why Appium with Python bindings?**

    1. Appium enables automation testing for mobile apps (Android and iOS) using a single framework.
    2. It supports multiple programming languages through the WebDriver protocol, making it flexible.
    3. It uses the WebDriver protocol, and the Selenium Python bindings implement that protocol, allowing 
       Python code to control mobile apps the same way Selenium controls web browsers.
    4. Using Python + Appium + Selenium bindings provides stable WebDriver APIs, better compatibility, and reusable design 
       patterns (e.g., Page Object Model, waits, locators).
    5. It enables cross-platform mobile automation (Android/iOS) with familiar Selenium-style commands while leveraging 
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
      config.ini        # store env, device and server settings
      pytest.ini        # init files
      README.md         # Instruction file.
      requirement.txt   # install dependencies

**Task description:**

    1.  Get the Mobile application(SimpleLogin) for Android(*.apk) and iOS(*.ipa))
    2.  Create tests(features and stories) for SimpleLogin app 
    
![Testcases](img.png)

    3. Stacks to create pytest mobile automation framework based on design pattern(POM - Page Object Model):
        - Appium
        - Python
        - pytest
        - Allure
    4.  Instructions given below for prerequisites, setup, and to run tests.

**Prerequisites and Setup istructions:**

    1. Install Python 3.12 (https://www.python.org/downloads/)
    2. Clone the repository to your local machine:  'mobile_simple_app'.
        - git clone https://github.com/saafihub/mobile_simple_app.git
        - cd mobile_simple_app
    3. Build the Project(Steps)
        1. pip install virtualenv
        2. To isolate virtual environment, Goto 'mobile_simple_app'> Type Command: 'python -m venv mobile_tests'
        3. To get isolated environment, Go to folder 'mobile_tests>Scripts' and Type: 'activate'
        4. Go back to root folder 'mobile_simple_app'
        5. To install all necessary packages, need to run this requirement file, Type: 'pip install -r requirements.txt'

**Andriod(emulators, real device, bluestacks)**

    1. Appium Server (https://github.com/appium/appium-desktop/releases/tag/v1.22.3-4) OR Install Node.js and Install Appium(<v2.0)
    2. Android Studio/SDK (https://developer.android.com/studio/install)
    3. Install android device emulator via device manager or plug real device or bluestacks
    4. Run android device (if you are working with emulator,real device or bluestacks. Check devices via cmd `adb devices` and copy current device name)
    5. Start run appium server or (CMD: 'appium') if installed via Node.js.

**IOS (need macOS)**

    1. Appium Server (https://github.com/appium/appium-desktop/releases/tag/v1.22.3-4)
    2. Install Xcode from App store to select simulator or plug real device 
    3. Install Carthage and set up WebDriverAgent
    4. Use Xcode to provisioning profile/Signing for WDAgentRunner target
    5. Run appium server

**To run tests locally(emulators, real device, bluestacks):**

    1. Check current device name in config.ini. If device name is not match with `CURRENT_DEVICE` change variable value to device name and details
    2. Run tests for android (example: `pytest test_android.py --runmode=local --alluredir=reports/allure-results or --html-report=./report/pytest_html_report.html`)
    3. Run tests for ios (example: `pytest test_ios.py --runmode=local --alluredir=reports/allure-results or --html-report=./report/pytest_html_report.html')

**To run tests in Browserstack:**

    1. Check browserstack set in config.ini correcly. If device name is not match with `BROWSERSTACK_DEVICES` change variable value to correct device name, credentials  and app details.
        - Can easily extend to other devices farms by adding driver and runmodes such as like saucelabs and other device farms etc. 
    2. Run tests for android (example: `pytest tests/test_android.py --runmode=browserstack --alluredir=reports/allure-results or --html-report=./report/pytest_html_report.html`)
    3. Run tests for ios (example: `pytest tests/test_ios.py --runmode=browserstack --alluredir=reports/allure-results or --html-report=./report/pytest_html_report.html')

**To run tests in parallel with multiple devices either with Browserstack or locally:**

    1. Local : pytest tests/test_android.py -n 2 --runmode=local --alluredir=reports/allure-results or --html-report=./report/pytest_html_report.html.
    2. Browserstack : pytest tests/test_android.py -n 2 --runmode=browserstack --alluredir=reports/allure-results or --html-report=./report/pytest_html_report.html

**To Re-Run failed tests to retries  either with Browserstack or locally:**

    1. Local : pytest tests/test_android.py --reruns 2 --reruns-delay 2  --runmode=local --alluredir=reports/allure-results or --html-report=./report/pytest_html_report.html.
    2. Browserstack : pytest tests/test_android.py --reruns 2 --reruns-delay 2  --runmode=browserstack --alluredir=reports/allure-results or --html-report=./report/pytest_html_report.html

**To run tests with tags(smoke, regression etc) :**

    1. Local : pytest tests/test_android.py -m smoke or regression --runmode=local --alluredir=reports/allure-results or --html-report=./report/pytest_html_report.html.
    2. Browserstack : pytest tests/test_android.py -m smoke or regression --runmode=browserstack --alluredir=reports/allure-results or --html-report=./report/pytest_html_report.html

**Report Formats**

    1. pytest-htmlreporter : pytest test_*.py --html-report=./report/pytest_html_report.html
    2. Allure Report : pytest test_*.py --alluredir=reports/allure-results
       (a). Collect allure report using command below to get this need to install allure commandline utility to view results.
            1. allure generate reports/allure-results -o reports/allure-report --clean
            2. allure open reports/allure-report










