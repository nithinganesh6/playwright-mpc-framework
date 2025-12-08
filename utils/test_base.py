from playwright.sync_api import Page

class TestBase:
    def __init__(self, page: Page):
        self.page = page

    def goto(self, path: str):
        return self.page.goto(path)
