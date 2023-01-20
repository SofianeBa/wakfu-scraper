import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--disable-extensions')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--remote-debugging-port=9222')


url = "https://www.wakfu.com/fr/mmorpg/encyclopedie/armures"
browser = webdriver.Chrome(chrome_options=options)
browser.get(url)
html_source = browser.page_source


with open(r".\html_wakfu.html", "w",encoding='utf-8') as file:
    file.write(html_source)


#print(html_source)
browser.quit()