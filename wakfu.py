# -*- coding: utf-8 -*-

from lxml import html
from lxml.html import HtmlElement

# Patch the HtmlElement class to add a function that can handle regular
# expressions within XPath queries.
def re_xpath(self, path):
    return self.xpath(path, namespaces={
        're': 'http://exslt.org/regular-expressions'})
HtmlElement.re_xpath = re_xpath

with open(r".\html_wakfu.html", "r",encoding='utf-8') as file:
    html_content = file.read()

tree = html.fromstring(html_content)

#print(tree.xpath("//div[@class='ak-main']/div/div[@class='ak-content']/div[@class='ak-title']"))
#print(tree.xpath("//div[@class='ak-mobile-menu-scroller']/div[@class='container ak-main-container']/div/div/div/main"))

# Type de l'objet
type_objet = tree.xpath("//div[@class='container ak-main-container']/div[@class='ak-main-content']/div[@class='ak-main-page']/div/main/div[@class='ak-container ak-main-center']/div/div[@class='ak-container ak-panel']/div/div/div[@class='col-sm-9']/div/div[@class='ak-encyclo-block-info ']/div/div[@class='ak-encyclo-detail-type col-xs-6']/span/text()")[0]
print("Type de l'objet:", type_objet)

# Nom de l'objet
nom_objet = tree.xpath("//div[@class='container ak-main-container']/div[@class='ak-main-content']/div[@class='ak-main-page']/div/main/div[@class='ak-container ak-main-center']/div/div[@class='ak-title-container ak-backlink']/h1/text()")[1].strip()
print("Nom de l'objet:", nom_objet)


# Rareté de l'objet
rarete_objet = (tree.xpath("//div[@class='ak-object-rarity']/span/text()")[1]).strip()
print("Rareté de l'objet:", rarete_objet)


# Niveau de l'objet
niveau_objet = tree.xpath("//div[@class='container ak-main-container']/div[@class='ak-main-content']/div[@class='ak-main-page']/div/main/div[@class='ak-container ak-main-center']/div/div[@class='ak-container ak-panel']/div/div/div[@class='col-sm-9']/div/div[@class='ak-encyclo-block-info ']/div/div[@class='ak-encyclo-detail-level col-xs-6 text-right']/text()")[0].strip().replace("Niveau : ","")
print("Niveau de l'objet:", niveau_objet)

# Liste des monstres qui peuvent le drop, avec pourcentage pour chacun
monstres = tree.xpath("//div[@class='ak-container ak-content-list ak-displaymode-image-col']/div[@class='row ak-container']/div/div/div/div/div[@class='ak-content']/div/a/span[contains(@data-hasqtip,'linker_monster')]/text()")
pourcentages = tree.xpath("//div[@class='ak-container ak-content-list ak-displaymode-image-col']/div[@class='row ak-container']/div/div/div/div/div[@class='ak-aside']/text()")

#print(tree.xpath("//div[@class='ak-main']/div[@class='ak-main-content']/div[@class='ak-title']/a[contains(@href, 'monstres')]/span/text()"))

#print(tree.xpath("//div[@class='ak-main']/div[@class='ak-main-content']"))
#print(tree.xpath("//div[@class='ak-main']/div")[1].get("class"))
#print(tree.xpath("//div[@class='ak-main']/div/div[@class='ak-content']/div[@class='ak-title']"))

drop_list = {}
for i in range(len(monstres)):
    drop_list[monstres[i]] = pourcentages[i]
print("Liste des Monstres qui peuvent le drop, avec pourcentage pour chacun:", drop_list)

# Sa recette, avec chaque objet, son type et sa quantité
recette_objets = tree.xpath("//div[@class='ak-container ak-panel ak-crafts']/div[@class='ak-panel-content']/div[@class='ak-container ak-panel']/div/div[@class='ak-container ak-content-list ak-displaymode-image-col']/div/div/div/div[@class='ak-main']/div/div[@class='ak-content']/div[@class='ak-title']/a/span/text()")

recette_types =tree.xpath("//div[@class='ak-container ak-panel ak-crafts']/div[@class='ak-panel-content']/div[@class='ak-container ak-panel']/div/div[@class='ak-container ak-content-list ak-displaymode-image-col']/div/div/div/div[@class='ak-main']/div/div[@class='ak-content']/div[@class='ak-text']/text()")

recette_quantites = tree.xpath("//div[@class='ak-container ak-panel ak-crafts']/div[@class='ak-panel-content']/div[@class='ak-container ak-panel']/div/div[@class='ak-container ak-content-list ak-displaymode-image-col']/div/div/div/div[@class='ak-front']/text()")

recette = {}
for i in range(len(recette_objets)):
    recette[" ".join(recette_objets[i].strip().replace('\n','').split())] = {"Type": " ".join(recette_types[i].strip().replace('\n','').split()), "Quantité": " ".join(recette_quantites[i].strip().replace('x','').replace('\n','').split())}

print("Sa recette, avec chaque objet, son type et sa quantité:", recette)
print(recette)