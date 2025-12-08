from playwright.sync_api import Page


class Header:
  def __init__(self, page: Page):
   self.page = page
   self.profile_icon = 'header .profile'
   self.logout_btn = 'text=Logout'


  def open_profile(self):
    self.page.click(self.profile_icon)


  def logout(self):
    self.open_profile()
    self.page.click(self.logout_btn)