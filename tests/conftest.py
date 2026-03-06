import os
import json
import os.path as ph
import pytest
import allure
from allure_commons.types import AttachmentType
from appium import webdriver
import warnings
import platform
import shutil
from datetime import datetime

warnings.filterwarnings(
    "ignore",
    category=UserWarning,
    message="Embedding username and password in URL could be insecure"
)

PAGE_LOAD_TIME = 30

LOCAL_HOST = "http://127.0.0.1:4723/wd/hub"
CURRENT_DEVICE = "emulator-5554"

APP_PATH_APK = ph.join(ph.dirname(__file__), "../app/SimpleLogin.apk")
ACTIVITY = "io.simplelogin.android.module.login.LoginActivity"

BROWSERSTACK_USERNAME = os.getenv("BROWSERSTACK_USERNAME", "saifsa_CATGHI")
BROWSERSTACK_ACCESS_KEY = os.getenv("BROWSERSTACK_ACCESS_KEY", "1r6vxyyXYSFNCY13Xf32")

APP_ID = "bs://0b3f38c292900b027c035fa3594e91c3a960333b"

BROWSERSTACK_DEVICES = [
    {"deviceName": "Samsung Galaxy S22", "platformVersion": "12.0"},
    {"deviceName": "Google Pixel 7", "platformVersion": "13.0"},
]
ALLURE_RESULTS_DIR = "reports/allure-results"
ALLURE_REPORT_DIR = "reports/allure-report"

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

    url = f"https://{BROWSERSTACK_USERNAME}:{BROWSERSTACK_ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub"

    return webdriver.Remote(url, caps)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when != "call":
        return

    driver = item.funcargs.get("driver")

    # ---------------- Allure Screenshot ----------------
    if report.failed and driver:
        try:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="Failure Screenshot",
                attachment_type=AttachmentType.PNG,
            )
        except Exception:
            pass

    # -------- Store result for teardown --------
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

