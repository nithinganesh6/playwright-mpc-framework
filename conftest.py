import os
from dotenv import load_dotenv
import pytest
from playwright.sync_api import sync_playwright


load_dotenv()


BASE_URL = os.getenv('BASE_URL', 'http://localhost:3000')


@pytest.fixture(scope='session')
def base_url():
  return BASE_URL


@pytest.fixture(scope='session')
def playwright_context():
    with sync_playwright() as p:
      yield p


@pytest.fixture
def page(playwright_context, base_url):
    browser = playwright_context.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(30000)
    page.goto(base_url)
    yield page
    context.close()
    browser.close()