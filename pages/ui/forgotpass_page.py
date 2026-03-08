import allure
from pages.locators.android_elements import CreateLogin

from pages.ui.base_page import BasePage


class ForgotPassPage(BasePage):
    """Class to interact with Forgot Password Page"""

    @allure.step('Click forgot password link on landing page')
    def click_forgot_pword(self):
        self.find_element(CreateLogin.forgot_pass, 'clickable').click()

    @allure.step('Get Security details of forgot password requests')
    def get_forgot_text(self):
        return self.find_element(CreateLogin.forgot_text).text

    @allure.step('Click Cancel action button on forgot password page')
    def click_cancel_btn(self):
        self.find_element(CreateLogin.forgot_cancel_btn, 'clickable').click()

    @allure.step('Check Forgot password header title')
    def get_forgot_header_text(self):
        return self.find_element(CreateLogin.forgot_header_id).text

    @allure.step('Enter Forgot password details in textfield')
    def forgot_email(self, email):
        self.find_element(CreateLogin.forgot_email_id).send_keys(email)

    @allure.step('Click Reset action button on forgot password page')
    def forgot_reset_btn(self):
        self.find_element(CreateLogin.forgot_reset_btn, 'clickable').click()

    @allure.step('Click Button which contains text "API"')
    def click_signin_apikey(self, getitem):
        getallbtns = self.find_elements(CreateLogin.get_all_buttons)
        for xerror in getallbtns:
            # xnerror = ['Sign in with API Key', 'Change API URL', 'LOG IN WITH PROTON']
            if xerror.text == getitem:
                xerror.click()

    @allure.step('Click x icon action on login to proton page')
    def proton_back_btn(self):
        # self.wait_element_visible(CreateLogin.close_proton)
        self.find_element(CreateLogin.close_proton, 'clickable').click()

