from pages.login_page import LoginPage

def test_login(page, base_url):
    login = LoginPage(page)
    #header = Header(page)
    login.navigate(base_url)
    login.login('nithin.ganeshan@streetlightdata.com', 'Usha@2024')
    login.verify_login()
    #header.logout()