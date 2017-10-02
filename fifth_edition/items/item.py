"""Base Item class"""

import fifth_edition.items.cost as cost
import csv

__author__ = "Grant Colasurdo"


class Item:
    def __init__(self, csv_row):
        self.name: str = csv_row['name']
        self.weight: float = csv_row['weight']
        self.volume: float = csv_row['volume']
        self.base_value: cost.Cost = cost.Cost(csv_row['cost'])


def new_item(item_name, parent_class) -> Item:
    item = None
    with open('items.csv', 'r') as file:
        item_db = csv.DictReader(file)
        for row in item_db:
            if row['item_name'] == item_name:
                class_to_call = parent_class
                item = class_to_call(row)

    return item
