import allure
import requests
import os
from allure_commons.types import AttachmentType
from selene.support.shared import browser
from dotenv import load_dotenv


def get_url_video(session_id: str):
    api_browserstack = os.getenv('API_BROWSERSTACK')
    session = requests.Session()
    auth = (os.getenv('LOGIN'), os.getenv('KEY'))
    response = session.get(
        f'{api_browserstack}/sessions/{session_id}.json', auth=auth).json()
    return response['automation_session']['video_url']


def add_video(session_id: str, name: str):
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + get_url_video(session_id) \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(html, name, AttachmentType.HTML, '.html')


def screenshot(*, name='screenshot'):
    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name=name,
        attachment_type=allure.attachment_type.PNG,
    )


def screen_xml_dump(*, name=None):
    allure.attach(
        browser.driver.page_source,
        name=name or 'page xml dump',
        attachment_type=allure.attachment_type.XML,
    )


def screen_html_dump(*, name=None):
    allure.attach(
        browser.driver.page_source,
        name=name or 'page html dump',
        attachment_type=allure.attachment_type.HTML,
    )
