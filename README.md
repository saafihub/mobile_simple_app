# mobile_app_testing_with_appium
A **Pytest-based automation framework** built using the **Page Object Model (POM)** with **Appium, Python, and Allure reporting** has been developed to test the **SimpleLogin mobile application for Mobile platforms(Android/iOS)**.

The framework is structured around **POM and Pytest fixtures**, enabling clear separation of responsibilities and better test organization. It supports multiple categories of testing, including **End-to-End (E2E), Functional, Compatibility, and Reliability testing** within a unified framework.

Designed with **scalability and extensibility** in mind, the framework allows additional test types to be integrated easily. By separating components such as **test logic, page objects, and test data**, it improves **maintainability, reusability, and overall test management**, making it easier to scale as the application evolves.


### Automated Testing Framework Design

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


### Test Architecture and Tools

1. **Tool & Language:** Appium with Python using Selenium bindings for mobile automation.  
2. **Design Pattern:** Page Object Model (POM) to ensure better code organization, reusability, and maintainability.  
3. **Testing Framework (Hybrid):** Implements a hybrid approach by combining **data-driven** and **keyword-driven** testing methodologies.  
4. **Continuous Integration:** Can be integrated with CI/CD tools such as **Jenkins** or **GitHub Actions** for automated test execution.


### Why Use Appium with Python Bindings?

1. **Cross-Platform Mobile Automation:**
   Appium allows automation testing for **both Android and iOS applications** using a single unified framework.

2. **Multi-Language Support:**
   Through the **WebDriver protocol**, Appium supports multiple programming languages, providing flexibility in choosing the preferred development language.

3. **WebDriver-Based Architecture:**
   Appium operates on the **WebDriver protocol**, and **Selenium’s Python bindings implement this protocol**, enabling Python scripts to control mobile applications in a similar way that Selenium automates web browsers.

4. **Stable and Reusable Automation Design:**
   The combination of **Python, Appium, and Selenium bindings** provides stable WebDriver APIs, improved compatibility, and supports reusable automation patterns such as **Page Object Model (POM), explicit waits, and structured locator strategies**.

5. **Efficient and Scalable Automation:**
   This stack enables **cross-platform mobile automation** using familiar **Selenium-style commands**, while benefiting from **Python’s simplicity, readability, and extensive testing ecosystem**.

### Framework Structure

```
├── app/            # Application binaries (*.apk, *.ipa)
├── pages/          # Page Object Model (POM) implementation
│   ├── locators/   # Repository of UI locators for application elements
│   ├── ui/         # Page classes encapsulating UI elements
│   ├── action/     # Methods and classes that perform actions on UI elements
├── data/           # Test data sources (e.g., JSON, Excel, etc.)
├── log/            # Generated execution logs
├── reports/        # Test execution reports and artifacts
├── utils/          # Utility modules (helpers, logger, common functions)
├── tests/          # Test cases / test runner files that trigger test execution
│
├── config.ini      # Environment, device, and Appium server configuration
├── pytest.ini      # Pytest configuration and markers
├── README.md       # Project documentation and usage instructions
└── requirements.txt # Project dependencies for installation
```


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














