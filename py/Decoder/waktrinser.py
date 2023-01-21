from core import Core
from models.LocaleSource import LocaleSource

class Waktrinser:
    def decode_string(self, localized_string: str, params: list, lvl_item: int) -> str:
        wsp_core = Core()
        return wsp_core.parse(LocaleSource(localized_string, params, lvl_item))

    def decode_effect(self, effect: dict, lvl_item: int, lang: str = 'fr') -> dict:
        effect['description'][lang] = self.decode_string(
            effect['description'][lang], effect['params'], lvl_item)
        return effect

    def decode_item(self, item: dict, lang: str = 'fr') -> dict:
        item['effects'] = [self.decode_effect(effect, item['lvl_item'], lang) for effect in item['effects']]
        return item

waktrinser = Waktrinser()
