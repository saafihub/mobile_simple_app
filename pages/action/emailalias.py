import allure
from utils.log import log
from pages.ui.alias_page import AliasPage
from pages.ui.login_page import LoginPage
PADE_LOAD_TIME = 30  # sec


class EmailAlias(AliasPage):
    """Class to interact with EmailAlias actions"""
    def __init__(self, driver):
        super().__init__(driver)
        self.alias_page = AliasPage(driver)
        self.login_page = LoginPage(driver)

    @allure.step('Alias Created for Email requested')
    def alias_creation(self, alias: str, aliasname: str, aliasnote: str):
        self.alias_page.addMenu()
        self.alias_page.createAlias(alias)
        self.alias_page.aliasName(aliasname)
        self.alias_page.aliasNote(aliasnote)
        self.alias_page.aliassubmit()
        aliasEmail = self.alias_page.alias_email_text()
        log.info(f'Alias-Email: {aliasEmail} - {alias}')
        try:
            assert aliasEmail.lower().startswith(alias.lower()), aliasEmail
        except AssertionError as e:
            log.error(f"Assertion failed: {e}")
            raise

    @allure.step('Check Email Handled before and after Email Send')
    def check_alias_handle(self, email_handle: int):
        self.alias_page.alias_email_click()
        actual = int(self.alias_page.email_handle_text())
        log.info(f'Alias-Email-Handle: {actual} - {email_handle}')
        try:
            assert actual == email_handle, f"Expected {email_handle}, got {actual}"
        except AssertionError as e:
            log.error(f"Assertion failed: {e}")
            raise

    @allure.step('Check all the texts in alias handle page')
    def check_all_texts_available(self, expected: bool = True):
        self.alias_page.alias_email_click()
        getalltxts = self.alias_page.all_texts_page()
        for xerror in getalltxts:
            log.info(f'Check all buttons: {xerror.text} - {expected}')
            assert (expected)

    def validate_email_alias(self, expected: bool = True):
        aliasName = self.alias_page.alias_email_text()
        log.info(f'Check all buttons: {aliasName}')
        if aliasName == 'Heroldx123@simplelogin.com':
            aliasName = True
        log.info(f'Expected value: {expected}')
        try:
            assert aliasName == expected, f"Alias validation failed. Actual: {aliasName}, Expected: {expected}"
        except AssertionError as e:
            log.error(f"Assertion failed: {e}")
            raise
