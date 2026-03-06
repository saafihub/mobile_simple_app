import allure
from pages.ui.alias_page import AliasPage
from pages.ui.contact_page import ContactPage
from pages.ui.login_page import LoginPage
from utils.log import log

PADE_LOAD_TIME = 30  # sec


class ContactAlias(ContactPage):
    """Class to interact with EmailAlias actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.contact_page = ContactPage(driver)
        self.alias_page = AliasPage(driver)
        self.login_page = LoginPage(driver)

    @allure.step('Alias Created for Email requested')
    def contact_creation(self, emailalias: str):
        self.alias_page.alias_email_send()
        self.contact_page.click_add_create()
        self.contact_page.click_manual_email_enter()
        self.contact_page.key_email_manually(emailalias)
        self.contact_page.createsubmit()
        aliasEmail = self.alias_page.alias_email_text()
        log.info(f'Contact-Create: {aliasEmail} - {emailalias}')
        try:
            assert emailalias, aliasEmail
        except AssertionError as e:
            log.error(f"Assertion failed: {e}")
            raise

    @allure.step('Check last Alias Email Send on')
    def contact_alias_email(self, subject, body, runmode):
        self.alias_page.alias_email_send()
        log.info('RUNMODE-2 : ' + str(runmode))
        if runmode == "local":
            self.alias_page.alias_email_click()
            self.contact_page.click_on_options()
            self.contact_page.enter_email_subject(subject)
            self.contact_page.enter_email_body(body)
            self.contact_page.emailSend()

    @allure.step('Check creation of Alias Email Send on')
    def contact_creation_email(self):
        CreationEmail = self.contact_page.get_created_email_contact()
        self.login_page.click_on_more_items()
        log.info(f'Contact-Creation-Alias-Email: {CreationEmail}')
        try:
            assert CreationEmail.startswith('Created on'), CreationEmail
        except AssertionError as e:
            log.error(f"Assertion failed: {e}")
            raise

    @allure.step('Check creation of Alias Email Send on')
    def contact_last_sent_email(self):
        lastEmail = self.contact_page.get_last_email_sent()
        self.login_page.click_on_more_items()
        log.info(f'Contact-Creation-Alias-Email: {lastEmail}')
        try:
            assert lastEmail.startswith('Last sent on'), lastEmail
        except AssertionError as e:
            log.error(f"Assertion failed: {e}")
            raise


