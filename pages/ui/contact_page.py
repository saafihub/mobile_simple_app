import allure
from pages.locators.android_elements import Aliascreate, CreateContact, \
    Commoncont, Labelcontent, GoogleEmail
from utils.log import log
from pages.ui.base_page import BasePage


class ContactPage(BasePage):
    """Class to interact with Contact Create Page"""

    @allure.step('Get text with Contact name')
    def get_text_contact(self, name: str):
        getallText = self.find_elements(Commoncont.PageTextview)
        if getallText:
            for xtext in getallText:
                if xtext.text == name:
                    return name

    @allure.step('Click on Add Menu Item (+)')
    def click_add_create(self):
        self.find_element(Aliascreate.addMenuitem).click()

    @allure.step('Check dialog available with the given title')
    def get_dialog_header_title(self):
        return self.find_element(Aliascreate.alertTitle).text

    @allure.step('Click the Email on the List Contact Create page')
    def click_manual_email_enter(self):
        try:
            getHeader = self.get_dialog_header_title()
            log.info(getHeader)
            if self.get_dialog_header_title() == 'Create new contact':
                self.find_element(Aliascreate.manageView).click()
        except Exception as e:
            log.error(str(e))
            pass

    @allure.step('Enter the Email Manually to create an email contact for alias')
    def key_email_manually(self, email: str):
        self.find_element(CreateContact.createEmail).send_keys(email)

    @allure.step('Submit the Manually to entered email to create')
    def createsubmit(self):
        self.find_element(CreateContact.createact).click()

    @allure.step('Cancel email not to create')
    def cancelsubmit(self):
        self.find_element(CreateContact.cancelact).click()

    @allure.step('Click on the Option as "Begin composing with default email" to the send email')
    def click_on_options(self):
        self.get_element_all(Commoncont.PageTextview, Labelcontent.composeemail).click()

    @allure.step('Enter the Subject on Google mail Composer')
    def enter_email_subject(self, subject):
        google_subject = self.find_element(GoogleEmail.emailSubject)
        google_subject.send_keys(subject)

    @allure.step('Enter the Body on Google mail Composer')
    def enter_email_body(self, body):
        google_body = self.find_element(GoogleEmail.emailbody)
        google_body.send_keys(body)

    @allure.step('Click on Google mail Composer to send email')
    def emailSend(self):
        self.find_element(GoogleEmail.emailSend).click()

    @allure.step('Check the last email sent from google composer with alias email')
    def get_last_email_sent(self):
        elements = self.find_elements(CreateContact.lastemailsent)
        if not elements:
            raise AssertionError("No lastemailsent elements for text found")
        return elements[0].text

    @allure.step('Check the creation email contract after sent from google composer with alias email')
    def get_created_email_contact(self):
        elements = self.find_elements(CreateContact.creationemail)
        if not elements:
            raise AssertionError("No Creationemail elements for text found")
        return elements[0].text
