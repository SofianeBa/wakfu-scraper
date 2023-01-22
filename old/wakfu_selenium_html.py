from selenium import webdriver
from lxml import html
from lxml.html import HtmlElement

options = webdriver.ChromeOptions()
options.add_argument('--disable-extensions')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--remote-debugging-port=9222')


url = "https://www.wakfu.com/fr/mmorpg/encyclopedie/armures/16811"
browser = webdriver.Chrome(chrome_options=options)
browser.get(url)
html_source = browser.page_source
tree = html.fromstring(html_source)

monstres = tree.xpath("//div[@class='ak-container ak-content-list ak-displaymode-image-col']/div[@class='row ak-container']/div/div/div/div/div[@class='ak-content']/div/a/span[contains(@data-hasqtip,'linker_monster')]/text()")
pourcentages = tree.xpath("//div[@class='ak-container ak-content-list ak-displaymode-image-col']/div[@class='row ak-container']/div/div/div/div/div[@class='ak-aside']/text()")

drop_list = {}
for i in range(len(monstres)):
    drop_list[monstres[i]] = pourcentages[i]
print("Liste des Monstres qui peuvent le drop, avec pourcentage pour chacun:", drop_list)

#with open(r".\html_wakfu.html", "w",encoding='utf-8') as file:
    #file.write(html_source)


#print(html_source)
browser.quit()