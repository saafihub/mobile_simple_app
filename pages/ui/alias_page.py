import allure
from pages.locators.android_elements import Commoncont, Aliascreate, \
    CreateContact, Emailhandle
from pages.ui.base_page import BasePage


class AliasPage(BasePage):
    """Class to interact with ui elements Alias Page """

    @allure.step('Click on Alias Addmenu(+) icon')
    def addMenu(self):
        self.find_element(Aliascreate.addMenuitem).click()

    @allure.step('Create an Alias for sender Email')
    def createAlias(self, alias: str):
        self.find_element(Aliascreate.prefixedit).send_keys(alias)

    @allure.step('Create an Alias Name for sender Email')
    def aliasName(self, aliasname: str):
        self.find_element(Aliascreate.createAliasname).send_keys(aliasname)

    @allure.step('Create an Alias Note for sender Email')
    def aliasNote(self, aliasnote: str):
        self.find_element(Aliascreate.aliasNote).send_keys(aliasnote)

    @allure.step('Click on submit to create an alias for sender Email')
    def aliassubmit(self):
        self.find_element(CreateContact.createact).click()

    @allure.step('Get text to validate')
    def get_text(self, textstr: str):
        return self.get_element_all(Commoncont.PageTextview, textstr).text

    @allure.step('Click on Alias name once Created from the alias created list')
    def alias_email_click(self):
        elements = self.find_elements(Aliascreate.emailtextView)
        if not elements:
            raise AssertionError("No emailTextView elements for click found")
        elements[0].click()

    @allure.step('Click on Send action to move page where contact email to create')
    def alias_email_send(self):
        elements = self.find_elements(Aliascreate.sendButton)
        if not elements:
            raise AssertionError("No sendButton elements found")
        elements[0].click()

    @allure.step('Get alias name from the alias created list')
    def alias_email_text(self):
        elements = self.find_elements(Aliascreate.emailtextView)
        if not elements:
            raise AssertionError("No emailTextView elements for text found")
        return elements[0].text

    @allure.step('Check email handle text to verify for email send to an contact email')
    def email_handle_text(self):
        handled_stat = self.find_element(Emailhandle.emailhandledstat)
        number_text = handled_stat.find_element(*Emailhandle.textall)
        return number_text.text

    @allure.step('Check email handle Stats to verify for email send to an contact email')
    def email_handle_stat(self):
        handled_stat = self.find_element(Emailhandle.emailhandledstat)
        type_text = handled_stat.find_element(*Emailhandle.typetext)
        return type_text.text

    @allure.step('Get all button text details of landing page')
    def all_texts_page(self):
        return self.find_elements(Commoncont.PageTextview)

