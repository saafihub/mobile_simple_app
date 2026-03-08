import allure
from pages.locators.android_elements import CreateLogin, Commoncont, Labelcontent
from appium.webdriver.common.appiumby import AppiumBy
from pages.ui.base_page import BasePage


class LoginPage(BasePage):
    """Class to interact with ui elements of Login Page"""

    @allure.step('Enter Email into textfield')
    def email(self, name: str):
        self.find_element(CreateLogin.Email_address).send_keys(name)

    @allure.step('Enter Password into textfield')
    def password(self, pword: str):
        self.find_element(CreateLogin.Pass_word).send_keys(pword)

    @allure.step('Click the login action to proceed to logged-in')
    def click_login(self):
        self.find_element(CreateLogin.Login_button, 'clickable').click()

    @allure.step('Navigate to Sign up Page')
    def click_sign_up(self):
        self.find_element(CreateLogin.Signup_button, 'clickable').click()

    @allure.step('Click the cancel action to back login page')
    def click_cancel(self):
        self.find_element(CreateLogin.Cancel_button, 'clickable').click()

    @allure.step('Message displayed, Required min 8 chars for password field')
    def get_error_pwdtext(self):
        return self.find_element(CreateLogin.email_pass_text_error).text

    @allure.step('Click the about us link @ bottom right cornor')
    def click_about_us(self):
        self.find_element(CreateLogin.About_us, 'clickable').click()

    @allure.step('Get SimpleLogin app version - 1.19.2')
    def get_sl_version(self):
        return self.find_element(CreateLogin.SL_app_version).text

    @allure.step('Error Message displayed for Invalid Login')
    def get_toast(self):
        return self.get_toast_text(Commoncont.ToastMessage)

    @allure.step('Title for About us page as "About SimpleLogin"')
    def get_bar_title(self):
        return self.find_element(CreateLogin.Toolbar_title).text

    @allure.step('Click the X mark to cancel about us back to login page')
    def click_cancel_image(self):
        self.find_element(CreateLogin.Cancel_image_button, 'clickable').click()

    @allure.step('Check SimpleLogin Image available')
    def sl_image_view(self):
        return self.find_element(CreateLogin.Image_view).is_displayed()

    @allure.step('Check Error displays on less than 8 chars')
    def Error_image_view(self):
        return self.find_element(CreateLogin.Error_icon).is_displayed()

    @allure.step('Get all text details of signup page')
    def all_error_signup(self):
        return self.find_elements(CreateLogin.email_pass_text_error)

    @allure.step('Get all button text details of landing page')
    def all_btns_landing(self):
        return self.find_elements(CreateLogin.get_all_buttons)

    @allure.step('Try Reset back to default value')
    def reset_image_view(self):
        self.find_element(CreateLogin.Image_view, 'clickable').click()

    @allure.step('Get SimpleLogin Success Login Validation')
    def get_success_login(self):
        return self.find_element(CreateLogin.success_login_text).text

    @allure.step('Scroll up down to visible text')
    def scroll_to_text(self, text):
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiScrollable(new UiSelector().scrollable(true))'
            f'.scrollIntoView(new UiSelector().text("{text}"))'
        )

    @allure.step('Click on more items Image')
    def click_on_more_items(self):
        # self.find_element(CreateLogin.moreitems).click()
        elements = self.find_elements(CreateLogin.moreitems)
        if not elements:
            raise AssertionError("No moreitem elements found")
        elements[0].click()

    @allure.step('Click on the Option as "Begin composing with default email" to the send email')
    def click_on_signout(self):
        self.get_element_all(Commoncont.MoreItemsView, Labelcontent.sign_out).click()

    def confirmSignout(self):
        self.find_element(CreateLogin.signmeout).click()

    def get_app_back_activate(self):
        self.get_app_back()


