from playwright.sync_api import Page, expect
from ai.smart_actions import smart_click, smart_fill
import re


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username = '#username'
        self.password = '#password'
        self.submit = 'button[type="submit"]'

    def navigate(self, base_url: str):
        self.page.goto(f"{base_url}/login")

    def login(self, user: str, pwd: str):
        smart_fill(self.page, "username field", self.username, user)
        smart_fill(self.page, "password field", self.password, pwd)
        smart_click(self.page, "submit button", self.submit)

    def verify_login(self):
        expect(self.page).to_have_url(re.compile(r".*/app.*"))

