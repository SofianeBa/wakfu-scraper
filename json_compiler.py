import json

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

with open('./Ressources/1.78.1.7/items.json') as json_file:
    items = json.load(json_file)
with open('./Ressources/1.78.1.7/actions.json') as json_file:
    actions = json.load(json_file)
with open('./Ressources/1.78.1.7/collectibleResources.json') as json_file:
    collectibleResources = json.load(json_file)
with open('./Ressources/1.78.1.7/equipmentItemTypes.json') as json_file:
    equipmentItemTypes = json.load(json_file)
with open('./Ressources/1.78.1.7/harvestLoots.json') as json_file:
    harvestLoots = json.load(json_file)
with open('./Ressources/1.78.1.7/itemProperties.json') as json_file:
    itemProperties = json.load(json_file)
with open('./Ressources/1.78.1.7/jobsItems.json') as json_file:
    jobsItems = json.load(json_file)
with open('./Ressources/1.78.1.7/recipeCategories.json') as json_file:
    recipeCategories = json.load(json_file)
with open('./Ressources/1.78.1.7/recipeIngredients.json') as json_file:
    recipeIngredients = json.load(json_file)
with open('./Ressources/1.78.1.7/recipeResults.json') as json_file:
    recipeResults = json.load(json_file)
with open('./Ressources/1.78.1.7/recipes.json') as json_file:
    recipes = json.load(json_file)
with open('./Ressources/1.78.1.7/resources.json') as json_file:
    resources = json.load(json_file)
with open('./Ressources/1.78.1.7/resourceTypes.json') as json_file:
    resourceTypes = json.load(json_file)
with open('./Ressources/1.78.1.7/states.json') as json_file:
    states = json.load(json_file)
    # Print the type of data variable
    #print("Type:", type(data))
 
    # Print the data of dictionary
    #print(data[0])

def find_item_type_name(item):
    id = item["definition"]["item"]["baseParameters"]["itemTypeId"]
    for value in equipmentItemTypes:
        if value["definition"]["id"] == id:
            return value["title"]["fr"]
    return -1



item["Nom"] = items[0]["title"]["fr"];
item["Description"] = items[0]["description"]["fr"];
item["Type"] = find_item_type_name(items[0])

#Rareté
#Niveau
#Drop (monstres + pourcentages)

#Recette : {type : Boulanger, Niveau : 53, Ingrédients : [{id objet : 1, nom objet : eau, quantité : 10}]}




print(item)