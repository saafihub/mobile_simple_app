from appium.webdriver.common.appiumby import AppiumBy


class CreateLogin:
    Signup_button = (AppiumBy.ID, 'io.simplelogin.android:id/signUpButton')
    Email_address = (AppiumBy.XPATH, '//*[contains(@text, "Email address")]')
    Pass_word = (AppiumBy.XPATH, '//*[contains(@text, "Password")]')
    Login_button = (AppiumBy.ID, 'io.simplelogin.android:id/loginButton')
    Cancel_button = (AppiumBy.ID, 'io.simplelogin.android:id/cancelButton')
    Pass_text_error = (AppiumBy.ID, 'io.simplelogin.android:id/textinput_error')  # Minimum 8 characters is required
    email_pass_text_error = (
        AppiumBy.CLASS_NAME, 'android.widget.TextView')  # Reset API URL to: https://app.simplelogin.io
    Error_icon = (AppiumBy.ACCESSIBILITY_ID, 'Error')
    About_us = (AppiumBy.ID, 'io.simplelogin.android:id/aboutUsTextView')  # About Us
    SL_app_version = (AppiumBy.ID, 'io.simplelogin.android:id/appVersionTextView')  # SimpleLogin v1.19.2
    Toast_message = (
        AppiumBy.XPATH, '//*[contains(@text, "Incorrect email or password")]')  # Incorrect email or password
    Toolbar_title = (AppiumBy.ID, 'io.simplelogin.android:id/toolbarTitleText')  # About SimpleLogin
    Cancel_image_button = (AppiumBy.CLASS_NAME, 'android.widget.ImageButton')
    Image_view = (AppiumBy.CLASS_NAME, 'android.widget.ImageView')
    forgot_pass = (AppiumBy.ID, 'io.simplelogin.android:id/forgotPasswordButton')  # Forgot password
    forgot_text = (
        AppiumBy.CLASS_NAME, 'android.widget.TextView')  # So make sure that you enter the correct email address.
    forgot_cancel_btn = (AppiumBy.ID, 'io.simplelogin.android:id/cancelButton')
    get_all_buttons = (AppiumBy.CLASS_NAME, 'android.widget.Button')
    forgot_header_id = (AppiumBy.ID, 'io.simplelogin.android:id/toolbarTitleText')
    forgot_email_id = (AppiumBy.XPATH, '//*[@resource-id="io.simplelogin.android:id/emailTextField"]')
    forgot_reset_btn = (AppiumBy.ID, 'io.simplelogin.android:id/resetButton')
    close_proton = (AppiumBy.ACCESSIBILITY_ID, 'Close tab')
    success_login_text = (AppiumBy.ID, 'io.simplelogin.android:id/noteTextView')
    aliasHeader = (AppiumBy.ID, 'io.simplelogin.android:id/toolbarTitleText')  # Your Aliases
    moreitems = (AppiumBy.XPATH,
                 '//android.view.ViewGroup[@resource-id="io.simplelogin.android:id/toolbar"]'
                 "//android.widget.ImageButton")
    all_items = (AppiumBy, '//*[@resource-id="io.simplelogin.android:id/design_menu_item_text"]')
    signmeout = (AppiumBy.XPATH, "//android.widget.Button[@text='Yes, sign me out']")


class Aliascreate:
    sendButton = (AppiumBy.XPATH, '//*[@resource-id="io.simplelogin.android:id/sendEmailButton"]')
    contactpage = (AppiumBy.ID, 'io.simplelogin.android:id/toolbarTitleText')
    addMenuitem = (AppiumBy.ID, 'io.simplelogin.android:id/addMenuItem')
    alertTitle = (AppiumBy.ID, 'io.simplelogin.android:id/alertTitle')
    manageView = (AppiumBy.XPATH, '//*[contains(@text, "Manually enter email address")]')
    prefixedit = (AppiumBy.ID, 'io.simplelogin.android:id/prefixEditText')
    createAliasname = (AppiumBy.ID, 'io.simplelogin.android:id/nameEditText')
    aliasNote = (AppiumBy.ID, 'io.simplelogin.android:id/noteEditText')
    emailtextView = (AppiumBy.XPATH, '//*[@resource-id="io.simplelogin.android:id/emailTextView"]')


class CreateContact:
    # createTitle = (AppiumBy.XPATH, '//*[contains(@text, "Create Contact")]')
    # createHeader = (AppiumBy.XPATH, '//*[contains(@text, "Create a contact to send email from your alias")]')
    # get_text_create = (AppiumBy.CLASS_NAME, 'android.widget.TextView')
    createEmail = (AppiumBy.XPATH, '//android.widget.EditText[@text="Email address"]')
    createact = (AppiumBy.ID, 'io.simplelogin.android:id/createButton')
    cancelact = (AppiumBy.ID, 'io.simplelogin.android:id/cancelButton')
    creationemail = (AppiumBy.ID, 'io.simplelogin.android:id/creationDateTextView')
    lastemailsent = (AppiumBy.ID, 'io.simplelogin.android:id/lastEmailSentTextView')


class Commoncont:
    PageTextview = (AppiumBy.CLASS_NAME, 'android.widget.TextView')
    MoreItemsView = (AppiumBy.CLASS_NAME, 'android.widget.CheckedTextView')
    ToastMessage = (AppiumBy.XPATH, '//*[@class="android.widget.Toast"]')
    Toast_message = (AppiumBy.XPATH, '//*[contains(@text,"personal inbox")]')


class Emailhandle:
    emailhandledstat = (AppiumBy.ID, 'io.simplelogin.android:id/handledStat')
    forwardstat = (AppiumBy.ID, 'io.simplelogin.android:id/forwardedStat')
    textall = (AppiumBy.ID, 'io.simplelogin.android:id/numberTextView')
    typetext = (AppiumBy.ID, 'io.simplelogin.android:id/typeTextView')


class GoogleEmail:
    emailSubject = (AppiumBy.ID, 'com.google.android.gm:id/subject')
    emailbody = (AppiumBy.XPATH,
                 "//android.widget.LinearLayout[@resource-id='com.google.android.gm:id/wc_body_layout']"
                 "//android.widget.EditText")
    emailSend = (AppiumBy.ACCESSIBILITY_ID, 'Send')


class Labelcontent:
    composeemail = 'Begin composing with default email'
    sign_out = 'Sign Out'
