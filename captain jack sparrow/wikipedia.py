from selenium import webdriver

def get_info(query):
        drive = webdriver.Chrome(executable_path=r'#################chrome drive path#################')
        drive.get(url='https://www.wikipedia.org/')
        drive.find_element('xpath','//*[@id="searchInput"]').send_keys(query)
        drive.find_element('xpath','//*[@id="search-form"]/fieldset/button').click()
        pasage = drive.find_element('xpath','//*[@id="mw-content-text"]/div[1]/p[2]')
        drive.minimize_window()
        return pasage
