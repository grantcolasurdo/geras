"""Equipment Parent Class"""

import fifth_edition.items.item as item

__author__ = "Grant Colasurdo"


class Equipment(item.Item):
    def __init__(self, item_name):
        super().__init__()