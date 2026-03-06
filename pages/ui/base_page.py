import allure
import time
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, WebDriverException
from utils.log import log
from waiting import wait

PADE_LOAD_TIME = 30  # sec
POLL_FREQUENCY = 0.2


class BasePage:
    """Class with common actions"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, PADE_LOAD_TIME)
        self.pollwait = WebDriverWait(self.driver, PADE_LOAD_TIME, POLL_FREQUENCY)

    @allure.step('Go back to previous page')
    def go_to_previous_page(self, hide_keyboard: bool = False):
        if hide_keyboard:
            self.hide_keyboard()
        self.driver.back()

    @allure.step('Wait until element is visible')
    def wait_element_visible(self, locator):
        return self.pollwait.until(EC.visibility_of_element_located(locator))

    @allure.step('Wait until element is visible')
    def wait_element_clickable(self, locator):
        return self.pollwait.until(EC.element_to_be_clickable(locator))

    @allure.step('Wait until element is to be present')
    def wait_element_presence(self, locator):
        return self.pollwait.until(EC.presence_of_element_located(locator))

    @allure.step('Hide keyboard')
    def hide_keyboard(self):
        wait(lambda: self.driver.is_keyboard_shown(),
             timeout_seconds=PADE_LOAD_TIME)
        self.driver.hide_keyboard()

    @allure.step('Perform Long Press')
    def long_press(self, element):
        TouchAction(self.driver).long_press(element).perform()

    @allure.step('Retrieve All Elements to check its on non stale to proceed')
    def find_element_all(self, locator, wait_type="visible"):  # , multiple=False):
        wait_strategies = {
            "visible": self.wait_element_visible,
            "present": self.wait_element_presence,
            "clickable": self.wait_element_clickable
        }
        # log.info(wait_strategies[wait_type])
        if wait_type not in wait_strategies:
            raise ValueError(f"Invalid wait_type: {wait_type}")

        wait_strategies[wait_type](locator)

    @allure.step('Retrieve a elements before Act upon it')
    def find_element(self, locator, wait_type="visible"):
        self.find_element_all(locator, wait_type=wait_type)  # wait once
        return self.driver.find_element(*locator)

    @allure.step('Retrieve all elements before Act upon it')
    def find_elements(self, locator, wait_type="visible"):
        self.find_element_all(locator, wait_type=wait_type)  # wait once
        return self.driver.find_elements(*locator)

    @allure.step('Get the extact element via text to be clickable or visible')
    def get_element_all(self, element: str, textname: str):
        getallText = self.find_elements(element)
        if getallText:
            for xtext in getallText:
                if xtext.text == textname:
                    return xtext

    @allure.step('get the toast message')
    def get_toast(self, locator):
        toast_element = self.pollwait.until(lambda d: d.find_element(*locator))
        return toast_element.text

    @allure.step('Find the element and get the toast message')
    def get_toast_text(self, toast_locator, timeout=5):
        end_time = time.time() + timeout
        while time.time() < end_time:
            try:
                toast = self.driver.find_element(*toast_locator)
                return toast.text
            except:
                pass
        raise Exception("Toast message not found")

    @allure.step('Stable retrival for ci')
    def get_toast_text_ci(self, expected_text, timeout=5):
        import time

        end_time = time.time() + timeout
        while time.time() < end_time:
            page_source = self.driver.page_source
            if expected_text in page_source:
                return expected_text
        raise Exception("Toast not found in page source")

    @allure.step('Click the items Safely with out flaky')
    def safe_element_visibility(self, locator, timeout=20, poll_frequency=0.5, max_retries=3):
        attempt = 0
        while attempt < max_retries:
            try:
                wait = WebDriverWait(self, timeout, poll_frequency, ignored_exceptions=[
                    StaleElementReferenceException, WebDriverException
                ])
                # element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
                # element.click()
                toast_element = wait.until(lambda d: d.find_element(*locator))
                return True  # success
            except (TimeoutException, StaleElementReferenceException, WebDriverException) as e:
                log.info(f"Attempt {attempt + 1} failed: {e}. Retrying...")
                time.sleep(1)
                attempt += 1
        raise Exception(f"Failed to click element after {max_retries} attempts: {locator}")

    def get_app_back(self):
        self.wait.until(lambda d: d.query_app_state("io.simplelogin.android") == 5)

