import json
import subprocess

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
            ingredient["item_name"] = find_item_name(value["itemId"])
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

item["ID"] = items[1000]["definition"]["item"]["id"]
item["Nom"] = items[1000]["title"]["fr"]
item["Niveau"] = items[1000]["definition"]["item"]["level"]
item["Type"] = find_item_type(items[1000])
item["Rareté"] = rarity[items[1000]["definition"]["item"]["baseParameters"]["rarity"]]
item["Description"] = items[1000]["description"]["fr"]
item["Effet"] = find_effects(items[1000])

id_recette = find_recipe_id(item["ID"])
if id_recette < 0:
    item["Recette"] = None
else:
    item["Recette"] = {}
    item["Recette"]["ID"] = id_recette
    item["Recette"]["Métier"] = find_recipe_job(id_recette)
    item["Recette"]["Ingrédients"] = find_recipe_ingredients(id_recette)
    


#Drop (monstres + pourcentages) A IMPLEMENTER PLUS TARD (besoin de scrap le site, non présent dans json)

#Recette : {type : Boulanger, Niveau : 53, Ingrédients : [{id objet : 1, nom objet : eau, quantité : 10}]}
#Nom des objets à récupérer via scraping




print(item)