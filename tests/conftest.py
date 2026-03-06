import os
import json
import pytest
import allure
import warnings
import platform
import shutil
from allure_commons.types import AttachmentType
from configparser import ConfigParser
from appium import webdriver
from utils.log import log
from datetime import datetime
warnings.filterwarnings(
    "ignore",
    category=UserWarning,
    message="Embedding username and password in URL could be insecure"
)

PAGE_LOAD_TIME = 30
config = ConfigParser()
config_path = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "config.ini"
)
config.read(config_path)

LOCAL_HOST = config.get("localrun", "LOCAL_HOST")
CURRENT_DEVICE = config.get("localrun", "CURRENT_DEVICE")
APP_PATH_APK = os.path.join(os.path.dirname(__file__), config.get("localrun", "APP_PATH_APK"))
ACTIVITY = config.get("localrun", "ACTIVITY")
BROWSERSTACK_USERNAME = config.get("devicefarm", "BROWSERSTACK_USERNAME")
BROWSERSTACK_ACCESS_KEY = config.get("devicefarm", "BROWSERSTACK_ACCESS_KEY")
APP_ID = config.get("devicefarm", "APP_ID")
BROWSERSTACK_DEVICES = config.get("devicefarm", "BROWSERSTACK_DEVICES")
ALLURE_RESULTS_DIR = config.get("reportallure", "ALLURE_RESULTS_DIR")
ALLURE_REPORT_DIR = config.get("reportallure", "ALLURE_REPORT_DIR")

def pytest_addoption(parser):
    parser.addoption(
        "--runmode",
        action="store",
        default="local",
        choices=["local", "browserstack"],
        help="Execution mode",
    )


@pytest.fixture(scope="session")
def runmode(request):
    return request.config.getoption("--runmode")

def _write_allure_environment(runmode):
    os.makedirs(ALLURE_RESULTS_DIR, exist_ok=True)

    device = CURRENT_DEVICE
    platform_version = "local"

    if runmode == "browserstack":
        device_index = int(os.getenv("DEVICE_INDEX", 0))
        device = BROWSERSTACK_DEVICES[device_index]["deviceName"]
        platform_version = BROWSERSTACK_DEVICES[device_index]["platformVersion"]

    env_data = [
        f"OS={platform.system()}",
        f"OS Version={platform.release()}",
        f"Python={platform.python_version()}",
        f"Automation=Pytest + Appium",
        f"RunMode={runmode}",
        f"Device={device}",
        f"Platform Version={platform_version}",
        f"Execution Time={datetime.now()}",
    ]

    with open(f"{ALLURE_RESULTS_DIR}/environment.properties", "w") as f:
        f.write("\n".join(env_data))

def _write_executor():
    executor_data = {
        "name": "Automation Execution",
        "type": "local",
        "buildName": "SimpleLogin Mobile Automation",
        "reportName": "Allure Mobile Automation Report",
    }

    with open(f"{ALLURE_RESULTS_DIR}/executor.json", "w") as f:
        json.dump(executor_data, f, indent=4)

def _copy_allure_history():
    history_src = f"{ALLURE_REPORT_DIR}/history"
    history_dest = f"{ALLURE_RESULTS_DIR}/history"

    if os.path.exists(history_src):
        shutil.copytree(history_src, history_dest, dirs_exist_ok=True)

def pytest_sessionstart(session):
    runmode = session.config.getoption("--runmode")

    os.makedirs(ALLURE_RESULTS_DIR, exist_ok=True)

    _write_allure_environment(runmode)
    _write_executor()
    _copy_allure_history()

@pytest.fixture(scope="function")
def driver(request):
    runmode = request.config.getoption("--runmode")

    if runmode == "local":
        drv = _get_local_driver()
    else:
        drv = _get_browserstack_driver(request)

    yield drv

    try:
        if runmode == "browserstack":
            result = getattr(request.node, "test_result", {})
            status = result.get("status", "failed")
            reason = result.get("reason", "Test failed")

            payload = {
                "action": "setSessionStatus",
                "arguments": {
                    "status": status,
                    "reason": reason[:250]
                }
            }

            drv.execute_script(
                f'browserstack_executor: {json.dumps(payload)}'
            )

        if drv and drv.session_id:
            drv.terminate_app("io.simplelogin.android")
            drv.quit()

    except Exception as e:
        print(f"[WARN] Teardown issue: {e}")

def _get_local_driver():
    caps = {
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "deviceName": CURRENT_DEVICE,
        "app": APP_PATH_APK,
        "appActivity": ACTIVITY,
        "noReset": True,
        "newCommandTimeout": 300,
    }
    log.info(f"Device: {CURRENT_DEVICE}")
    return webdriver.Remote(LOCAL_HOST, caps)

def _get_browserstack_driver(request):
    device_index = int(os.getenv("DEVICE_INDEX", 0))
    device = BROWSERSTACK_DEVICES[device_index]

    caps = {
        "platformName": "Android",
        "deviceName": device["deviceName"],
        "platformVersion": device["platformVersion"],
        "app": APP_ID,

        "project": "SimpleLogin",
        "build": f"Build-{device['deviceName']}",
        "name": request.node.name,

        "browserstack.debug": True,
        "browserstack.disableAnimations": True,
        "browserstack.idleTimeout": 300,
        "browserstack.networkLogs": True,
        "browserstack.consoleLogs": "info",
    }
    log.info(f"Device: {device}")
    url = f"https://{BROWSERSTACK_USERNAME}:{BROWSERSTACK_ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub"

    return webdriver.Remote(url, caps)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when != "call":
        return

    driver = item.funcargs.get("driver")

    if report.failed and driver:
        try:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="Failure Screenshot",
                attachment_type=AttachmentType.PNG,
            )
        except Exception:
            pass

    if report.failed:
        reason = report.longreprtext[:200].replace('"', "'")
        item.test_result = {"status": "failed", "reason": reason}
    else:
        item.test_result = {"status": "passed", "reason": "Test passed"}

@pytest.fixture(autouse=True)
def _add_device_labels(request):
    runmode = request.config.getoption("--runmode")

    if runmode == "local":
        allure.dynamic.label("device", CURRENT_DEVICE)
        allure.dynamic.label("execution", "local")

    else:
        device_index = int(os.getenv("DEVICE_INDEX", 0))
        device = BROWSERSTACK_DEVICES[device_index]

        allure.dynamic.label("device", device["deviceName"])
        allure.dynamic.label("platformVersion", device["platformVersion"])
        allure.dynamic.label("execution", "browserstack")
