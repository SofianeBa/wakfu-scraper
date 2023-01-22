import json
import subprocess
from selenium import webdriver
from lxml import html
import time
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service



options = Options()
ua = UserAgent()
userAgent = ua.random
print(userAgent)
options.add_argument(f'user-agent={userAgent}')
options.add_argument('--headless')
options.add_argument('--disable-extensions')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('disable-infobars')
options.add_argument('--disable-dev-shm-usage')

service = Service(r'C:\Users\sofia\Downloads\chromedriver_win32\chromedriver.exe')
service.start()
browser = webdriver.Chrome(options=options, service=service)
url = "https://www.wakfu.com/fr/mmorpg/encyclopedie/armures/"
#monstres = tree.xpath("//div[@class='ak-container ak-content-list ak-displaymode-image-col']/div[@class='row ak-container']/div[@class='ak-column ak-container col-xs-12 col-md-6']/div/div/div/div[@class='ak-content']/div/a/span/text()")
#pourcentages = tree.xpath("//div[@class='ak-container ak-content-list ak-displaymode-image-col']/div[@class='row ak-container']/div/div/div/div/div[@class='ak-aside']/text()")

#print(driver.page_source)
#driver.quit()


start_time = time.time()

#options = webdriver.ChromeOptions()
#options.add_argument('--disable-extensions')
#options.add_argument('--disable-gpu')
#options.add_argument('--no-sandbox')
#options.add_argument('start-maximized')
#options.add_argument('disable-infobars')
#options.add_argument('--disable-dev-shm-usage')
#options.add_argument('--remote-debugging-port=9222')
#url = "https://www.wakfu.com/fr/mmorpg/encyclopedie/armures/"
#browser = webdriver.Chrome(chrome_options=options)

version = "1.78.1.7"
chemin = "../Ressources/"
rarity = ["Commun","Inhabituel","Rare","Mythique","Légendaire","Relique","Souvenir","Épique"]

items = {}
actions = {}
collectibleResources = {}
equipmentItemTypes = {}
harvestLoots = {}
itemProperties = {}
jobsItems = {}
recipeCategories = {}
recipeIngredients = {}
recipeResults = {}
recipes = {}
resources = {}
resourceTypes = {}
states = {}
item = {}

with open(chemin+version+'/items.json') as json_file:
    items = json.load(json_file)
with open(chemin+version+'/actions.json') as json_file:
    actions = json.load(json_file)
with open(chemin+version+'/collectibleResources.json') as json_file:
    collectibleResources = json.load(json_file)
with open(chemin+version+'/equipmentItemTypes.json') as json_file:
    equipmentItemTypes = json.load(json_file)
with open(chemin+version+'/harvestLoots.json') as json_file:
    harvestLoots = json.load(json_file)
with open(chemin+version+'/itemProperties.json') as json_file:
    itemProperties = json.load(json_file)
with open(chemin+version+'/jobsItems.json') as json_file:
    jobsItems = json.load(json_file)
with open(chemin+version+'/recipeCategories.json') as json_file:
    recipeCategories = json.load(json_file)
with open(chemin+version+'/recipeIngredients.json') as json_file:
    recipeIngredients = json.load(json_file)
with open(chemin+version+'/recipeResults.json') as json_file:
    recipeResults = json.load(json_file)
with open(chemin+version+'/recipes.json') as json_file:
    recipes = json.load(json_file)
with open(chemin+version+'/resources.json') as json_file:
    resources = json.load(json_file)
with open(chemin+version+'/resourceTypes.json') as json_file:
    resourceTypes = json.load(json_file)
with open(chemin+version+'/states.json') as json_file:
    states = json.load(json_file)
    # Print the type of data variable
    #print("Type:", type(data))
 
    # Print the data of dictionary
    #print(data[0])

def find_item_type(item):
    id = item["definition"]["item"]["baseParameters"]["itemTypeId"]
    for value in equipmentItemTypes:
        if value["definition"]["id"] == id:
            return value["title"]["fr"]
    return "Inconnu"

def find_recipe_id(item_id):
    for value in recipeResults:
        if value["productedItemId"] == item_id:
            return value["recipeId"]
    return -1

def find_item_name(item_id):
    for value in items:
        if value["definition"]["item"]["id"] == item_id:
            return value["title"]["fr"]
    return "Inconnu"

def find_recipe_ingredients(recipe_id):
    ingredients = []
    for value in recipeIngredients:
        ingredient = {}
        if(value["recipeId"] == recipe_id):
            ingredient["item_id"] = value["itemId"]
            #This name search only work with equipments... To make it work with ressources, we have to find where they are hidden (not in the jsons...)
            ingredient["item_name"] = find_item_name_scraper(ingredient["item_id"])
            ingredient["quantity"] = value["quantity"]
            ingredients.append(ingredient)
    if len(ingredients):
        return ingredients
    else:
        #Here we have an error, because we found a recipe but the recipe has no ingredients....
        return None

def find_job_name(category_id):
    for value in recipeCategories:
        if (value["definition"]["id"] == category_id):
            return value["title"]["fr"]
    return "Inconnu"


def find_recipe_job(recipe_id):
    metier = {}
    for value in recipes:
        if(value["id"] == recipe_id):
            metier["Nom"] = find_job_name(value["categoryId"])
            metier["Niveau"] = value["level"]
            return metier
    metier["Nom"] = "Inconnu"
    metier["Niveau"] = "Inconnu"
    return

def find_effect_desc(action_id):
    for value in actions:
        if(value["definition"]["id"] == action_id):
            return value["description"]["fr"]
    return "Inconnu"

def find_effects(item):
    effects = []
    for value in item["definition"]["equipEffects"]:
        params = value["effect"]["definition"]["params"]
        description = find_effect_desc(value["effect"]["definition"]["actionId"])
        decoded_description = subprocess.run(["node", "./Decoder/decoder.js", description, json.dumps(params),str(item["definition"]["item"]["level"])], capture_output=True, text=True, encoding='utf-8')

        if (description != "Inconnu"):
            effect = {}
            effect["ID"] = value["effect"]["definition"]["actionId"]
            effect["Paramètres"] = params
            effect["Effet"] = decoded_description.stdout.strip()
            effects.append(effect)
    if(effects):
        return effects
    return "Inconnu"

def give_html_source(url):
    browser.get(url)
    return browser.page_source

def find_drop(item_id):
    #Let's find the drop on the internet
    html_source = give_html_source(url+str(item_id))
    tree = html.fromstring(html_source)
    monstres = tree.xpath("//div[@class='ak-container ak-content-list ak-displaymode-image-col']/div[@class='row ak-container']/div[@class='ak-column ak-container col-xs-12 col-md-6']/div/div/div/div[@class='ak-content']/div/a/span/text()")
    pourcentages = tree.xpath("//div[@class='ak-container ak-content-list ak-displaymode-image-col']/div[@class='row ak-container']/div/div/div/div/div[@class='ak-aside']/text()")
    drop_list = {}
    for i in range(len(monstres)):
        drop_list[monstres[i]] = pourcentages[i]
    return drop_list

def find_item_name_scraper(item_id):
    html_source = give_html_source(url+str(item_id))
    tree = html.fromstring(html_source)
    name = tree.xpath("//div[@class='container ak-main-container']/div[@class='ak-main-content']/div[@class='ak-main-page']/div/main/div[@class='ak-container ak-main-center']/div/div[@class='ak-title-container ak-backlink']/h1/text()")[1].strip()
    return name

item["ID"] = items[1001]["definition"]["item"]["id"]
item["Nom"] = items[1001]["title"]["fr"]
item["Niveau"] = items[1001]["definition"]["item"]["level"]
item["Type"] = find_item_type(items[1001])
item["Rareté"] = rarity[items[1001]["definition"]["item"]["baseParameters"]["rarity"]]
item["Description"] = items[1001]["description"]["fr"]
item["Effet"] = find_effects(items[1001])


id_recette = find_recipe_id(item["ID"])
if id_recette < 0:
    item["Recette"] = None
else:
    item["Recette"] = {}
    item["Recette"]["ID"] = id_recette
    item["Recette"]["Métier"] = find_recipe_job(id_recette)
    item["Recette"]["Ingrédients"] = find_recipe_ingredients(id_recette)

item["Drop"] = find_drop(item["ID"])



browser.quit()
print(item)

print("--- %s seconds ---" % (time.time() - start_time))