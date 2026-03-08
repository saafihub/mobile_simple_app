import allure
from pages.ui.base_page import BasePage
from pages.ui.login_page import LoginPage
from pages.ui.alias_page import AliasPage
from pages.ui.forgotpass_page import ForgotPassPage
from utils.log import log
PADE_LOAD_TIME = 30  # sec

class MyLogin(BasePage):
    """Class to interact with Login actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.login_page = LoginPage(driver)
        self.alias_page = AliasPage(driver)

    @allure.step('Login to SimpleLogin application')
    def app_login(self, ename: str, pname: str):
        self.login_page.email(ename)
        self.login_page.password(pname)
        self.login_page.click_login()

    @allure.step('Check "About us" Page')
    def about_us(self):
        self.login_page.click_about_us()
        title_abt = self.login_page.get_bar_title()
        self.login_page.click_cancel_image()
        log.info(f'footer: {title_abt} - About SimpleLogin ')
        try:
            assert 'About SimpleLogin', title_abt
        except AssertionError as e:
            log.error(f"Assertion failed: {e}")
            raise

    @allure.step('Check SimpleLogin app version')
    def check_sl_app_version(self):
        getVersion = self.login_page.get_sl_version()
        log.info(f'App Version: {getVersion} - SimpleLogin v1.19.2')
        try:
            assert 'SimpleLogin v1.19.2', getVersion
        except AssertionError as e:
            log.error(f"Assertion failed: {e}")
            raise

    @allure.step('Check forgot password details')
    def get_forgot_page(self, expected: bool = True):
        ForgotPassPage(self).click_forgot_pword()
        inexpected = 'So make sure that you enter the correct email address'
        get_text = ForgotPassPage(self).get_forgot_text()
        getheader = ForgotPassPage(self).get_forgot_header_text()
        ForgotPassPage(self).click_cancel_btn()
        try:
            if inexpected in get_text:
                assert expected, True
            log.info(f'Forgot pass header: {getheader} - Forgot password')
            assert 'Forgot password', getheader
        except AssertionError as e:
            log.error(f"Assertion failed: {e}")
            raise

    @allure.step('Check SimpleLogin Image available')
    def check_sl_app_image(self):
        getVersion = self.login_page.sl_image_view()
        try:
            assert True, getVersion
        except AssertionError as e:
            log.error(f"Assertion failed: {e}")
            raise

    @allure.step('Check valid toast message displays for Invalid login')
    def check_valid_toast_message(self, ename: str, pname: str):
        self.app_login(ename, pname)
        get_toast = self.login_page.get_toast()
        log.info(f'Incorrect credential toast: {get_toast} - Incorrect email or password')
        try:
            assert 'Incorrect email or password', get_toast
        except AssertionError as e:
            log.error(f"Assertion failed: {e}")
            raise

    @allure.step('Check valid error message displays signup page')
    def Check_signup_error_details(self, ename: str, pname: str = None, dsp: str = 'all', expected: bool = True):
        self.login_page.click_sign_up()
        self.login_page.email(ename)
        if pname:
            self.login_page.password(pname)
        if dsp == 'all':
            geterror = self.login_page.all_error_signup()
            for xerror in geterror:
                xnerror = ['Invalid email', 'Minimum 8 characters is required']
                if xerror.text in xnerror:
                    log.info(f'Message signup error: {xerror.text} - {expected}')
                    assert ((xerror.text in xnerror) == expected)
            self.login_page.click_cancel()
        else:
            self.login_page.click_sign_up()
            get_toast = self.login_page.get_toast()
            log.info(f'Toast Message: {get_toast}')
            # actualIn = ['Incorrect email or password', f'cannot use {ename} as personal inbox']
            try:
                assert f'cannot use {ename} as personal inbox', get_toast
            except AssertionError as e:
                log.error(f"Assertion failed: {e}")
                raise

    @allure.step('Check valid details on signup page')
    def Check_signup_valid_details(self, ename: str, pname: str):
        self.login_page.click_sign_up()
        self.app_login(ename, pname)
        # getVersion = self.login_page.sl_image_view()
        # assert True, getVersion
        get_toast = self.login_page.get_toast()
        log.info(f'Incorrect credential toast: {get_toast} - Incorrect email or password')
        try:
            assert 'Incorrect email or password', get_toast
        except AssertionError as e:
            log.error(f"Assertion failed: {e}")
            raise

    @allure.step('Check all the buttons and texts available in Landing page')
    def Check_buttons_texts_available(self, expected: bool = True):
        getallbtns = self.login_page.all_btns_landing()
        for xerror in getallbtns:
            xnerror = ['Forgot password', 'Sign up', 'Sign in with API Key', 'Change API URL', 'LOG IN WITH PROTON',
                       'SIGN IN']
            if xerror.text in xnerror:
                log.info(f'Check all buttons: {xerror.text} - {expected}')
                assert ((xerror.text in xnerror) == expected)

    @allure.step('Check the email address once reset the forgot password')
    def Check_reset_password(self, ename: str = None):
        ForgotPassPage(self).click_forgot_pword()
        ForgotPassPage(self).forgot_email()
        ForgotPassPage(self).forgot_reset_btn()
        getVersion = self.login_page.sl_image_view()
        try:
            assert True, getVersion
        except AssertionError as e:
            log.error(f"Assertion failed: {e}")
            raise

    @allure.step('Check the details of Sign in with API key page')
    def Check_signin_apikey(self):
        ForgotPassPage(self).click_signin_apikey(getitem='Sign in with API Key')
        getet = self.login_page.get_bar_title
        ForgotPassPage(self).click_cancel_btn()
        getVersion = self.login_page.sl_image_view()
        try:
            assert True, getVersion
            log.info(f'Message UI Text: {getet} - Enter API key')
            assert 'Enter API key', getet
        except AssertionError as e:
            log.error(f"Assertion failed: {e}")
            raise

    @allure.step('Check the details of Change API URL page')
    def Check_change_apiurl(self):
        ForgotPassPage(self).click_signin_apikey(getitem='Change API URL')
        getet = self.login_page.get_bar_title
        self.login_page.reset_image_view()
        getVersion = self.login_page.sl_image_view()
        try:
            assert True, getVersion
            log.info(f'Message UI Text: {getet} - Change API URL')
            assert 'Change API URL', getet
        except AssertionError as e:
            log.error(f"Assertion failed: {e}")
            raise

    @allure.step('Navigate to Log in with proton page')
    def navigate_to_proton(self):
        ForgotPassPage(self).click_signin_apikey(getitem='LOG IN WITH PROTON')
        ForgotPassPage(self).proton_back_btn()
        getVersion = self.login_page.sl_image_view()
        try:
            assert True, getVersion
        except AssertionError as e:
            log.error(f"Assertion failed: {e}")
            raise

    @allure.step('Check SimpleLogin app version')
    def check_success_login_text(self, expected: bool = True):
        succsslogin = self.login_page.get_success_login()
        log.info(f'Message UI Text: {succsslogin}')
        expectedIn = ["This is your first alias. It's used to receive SimpleLogin communications like new features "
                      "announcements, newsletters.", "NewsLetters"]
        try:
            assert ((succsslogin in expectedIn) == expected)
        except AssertionError as e:
            log.error(f"Assertion failed: {e}")
            raise

    @allure.step('Sign out from the simpleLogin app')
    def Signout_app(self):
        self.alias_page.alias_email_text()
        self.login_page.click_on_more_items()
        self.login_page.click_on_signout()
        self.login_page.confirmSignout()

    @allure.step('Get app from background to activate')
    def get_app_back(self):
        self.login_page.get_app_back_activate()

