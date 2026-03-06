import allure
import pytest
import json, time
import os.path as ph
import subprocess
from pages.action.mylogin import MyLogin
from pages.action.emailalias import EmailAlias
from pages.action.contactalias import ContactAlias
from utils.data_generator import get_random_string, get_current_date_and_time

testdata = ph.join(ph.dirname(__file__), "../data/cases.json")
# Load JSON data
with open(testdata) as f:
    test_data = json.load(f)
signup_data = [(v['ename'], v['pname'], v['dsp']) for v in test_data["signup_cases"].values()]
login_data = [(v['ename'], v['pname']) for v in test_data["login_cases"].values()]


@allure.feature("SimpleLogin Home Page")
@allure.story("Landing Page with valid Version")
@allure.description(
    """
    Test to check Landing Page by default 
    Test steps:
    1. Open app
    2. Check app launched with app version available in landing page
    """)
def test_landing_page_once_launch(driver):
    MyLogin(driver).check_sl_app_version()
    MyLogin(driver).check_sl_app_image()


@allure.feature("SimpleLogin Home Page")
@allure.story("Verify labels and buttons on Landing Page")
@allure.description(
    """
    Test to check Landing Page by default 
    Test steps:
    1. Open app
    2. Check the given button labals/texts  in landing page
    """)
def test_given_landingpage_details_button_texts(driver):
    MyLogin(driver).Check_buttons_texts_available()


@allure.feature("SimpleLogin Home Page")
@allure.story("validate the Sign up with invalid/valid details")
@allure.description(
    """
    Test to try sign up new user with invalid email and password 
    Test steps:
    1. Open app
    2. Click Sign up link
    3. Enter invalid details on email and password fields
    4. Check appropriate banner message displays.
    """)
@pytest.mark.parametrize("ename,pname,dsp", signup_data)
def test_signup_details(driver, ename, pname, dsp):
    MyLogin(driver).Check_signup_error_details(ename=ename, pname=pname, dsp=dsp)


@allure.feature("SimpleLogin Home Page")
@allure.story("validate the Sign up with invalid/valid details")
@allure.description(
    """
    Test user with valid details
    Test steps:
    1. Open app
    2. Click Sign In
    3. Enter valid details on email and password fields
    4. Moved to Alias page with Appropriate text should display.
    """)
@pytest.mark.parametrize("ename,pname", login_data)
def test_given_valid_details_success_login(driver, ename, pname):
    # ename = 'ssisaa01@gmail.com'
    # pname = 'saeed12345678'
    MyLogin(driver).app_login(ename=ename, pname=pname)
    MyLogin(driver).check_success_login_text()


@allure.feature("SimpleLogin Alias Creation")
@allure.story("Creation of alias for simplelogin emails ")
@allure.description(
    """
    Test user with valid details
    Test steps:
    1. Open app
    2. Click Sign In
    3. Enter valid details on email and password fields
    4. Moved to Alias page with Appropriate text should display.
    """)
@pytest.mark.parametrize("ename,pname", login_data)
def test_create_alias_for_an_email(driver, ename, pname):
    #ename = 'ssisaa01@gmail.com'
    #pname = 'saeed12345678'
    MyLogin(driver).app_login(ename=ename, pname=pname)
    aliasx = get_random_string(6)
    EmailAlias(driver).alias_creation(alias=aliasx, aliasname=get_random_string(12), aliasnote='NewsLetters')


@allure.feature("SimpleLogin Alias Creation")
@allure.story("Check handles of alias creation for simplelogin emails ")
@allure.description(
    """
    Test user with valid details
    Test steps:
    1. Open app
    2. Click Sign In
    3. Enter valid details on email and password fields
    4. Check Email handles after alias have been created
    """)
@pytest.mark.parametrize("ename,pname", login_data)
def test_alias_email_handle_validate(driver, ename, pname):
    #ename = 'ssisaa01@gmail.com'
    #pname = 'saeed12345678'
    MyLogin(driver).app_login(ename=ename, pname=pname)
    EmailAlias(driver).check_alias_handle(email_handle=0)


@allure.feature("SimpleLogin Alias Contact Creation")
@allure.story("Creation of contact for an alias emails ")
@allure.description(
    """
    Test user with valid details
    Test steps:
    1. Open app
    2. Click Sign In
    3. Enter valid details on email and password fields
    4. Once Alias get created, Try create an Contact email for that alias email.
    """)
@pytest.mark.parametrize("ename,pname", login_data)
def test_contact_alias_email_creation(driver, ename, pname):
    #ename = 'ssisaa01@gmail.com'
    #pname = 'saeed12345678'
    MyLogin(driver).app_login(ename=ename, pname=pname)
    ContactAlias(driver).contact_creation(emailalias='ssisaa7@gmail.com')


@allure.feature("SimpleLogin Alias Contact Creation")
@allure.story("Send an email to Contact via created alias email ")
@allure.description(
    """
    Test user with valid details
    Test steps:
    1. Open app
    2. Click Sign In
    3. Enter valid details on email and password fields
    4. Once Contact Email is created, Send an Email with an Alias as Sender.
    """)
@pytest.mark.parametrize("ename,pname", login_data)
def test_send_alias_email_contact(driver, runmode, ename, pname):
    #ename = 'ssisaa01@gmail.com'
    #pname = 'saeed12345678'
    MyLogin(driver).app_login(ename=ename, pname=pname)
    dnow = get_current_date_and_time()
    ContactAlias(driver).contact_alias_email(subject='Test Message subject(' + dnow + ')',
                                             body='Test Message Body (' + dnow + ')', runmode=runmode)
    ContactAlias(driver).contact_creation_email()
    MyLogin(driver).Signout_app()


@allure.feature("SimpleLogin Session Retain")
@allure.story("Validate the session for simplelogin via activate app from background")
@allure.description(
    """
    Test user with valid details
    Test steps:
    1. Open app
    2. Click Sign In
    3. Enter valid details on email and password fields
    4. Send app to background (simulate interruption)
    5. simulate memory pressure using Android Monkey
    6. Resume app to check session Valid to proceed to next steps.should not get reset.
    """)
@pytest.mark.parametrize("ename,pname", login_data)
def test_session_retained_after_background(driver, runmode, ename, pname):
    #ename = 'ssisaa01@gmail.com'
    #pname = 'saeed12345678'
    MyLogin(driver).app_login(ename=ename, pname=pname)
    MyLogin(driver).check_success_login_text()

    driver.background_app(30)  # 0.5 minutes
    subprocess.run(
        [
            "adb", "shell", "monkey",
            "-p", "io.simplelogin.android",
            "-c", "android.intent.category.LAUNCHER", "20"
        ],
        capture_output=True
    )

    driver.activate_app("io.simplelogin.android")
    driver.implicitly_wait(5)
    dnow = get_current_date_and_time()
    EmailAlias(driver).check_all_texts_available()
    if runmode == 'local':
        MyLogin(driver).login_page.click_on_more_items()
        MyLogin(driver).Signout_app()


@allure.feature("SimpleLogin Alias Creation")
@allure.story("Verify the created alias ")
@allure.description(
    """
    Test user with valid details
    Test steps:
    1. Open app
    2. Click Sign In
    3. Enter valid details on email and password fields
    4. Validate alias name created name as 'Heroldx123@simplelogin.com'.
    """)
@pytest.mark.parametrize("ename,pname", login_data)
def test_alias_email_name(driver, ename, pname):
    #ename = 'ssisaa01@gmail.com'
    #pname = 'saeed12345678'
    MyLogin(driver).app_login(ename=ename, pname=pname)
    EmailAlias(driver).validate_email_alias()
