import sys, os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

print(f"[conftest] loaded. wd={os.getcwd()}")
print(f"[conftest] python={sys.executable}")
print(f"[conftest] sys.path[0]={sys.path[0]}")

def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        default="en",
        help="UI language, e.g. en, es, fr, ru"
    )

@pytest.fixture
def browser(request):
    lang = request.config.getoption("language")
    print(f"[conftest] browser fixture init, language={lang}")
    options = webdriver.ChromeOptions()
    prefs = {"intl.accept_languages": lang}
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    print(f"[debug] language={lang}")

    yield driver
    driver.quit()